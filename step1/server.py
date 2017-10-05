#!/usr/bin/python
# coding: utf-8
"""A simple webserver."""

# python 2.7 compatibility
from __future__ import print_function, unicode_literals

# based on tornado
import tornado.ioloop
import tornado.web
import tornado.websocket

import sys
import json
import random

from translate import translate_text

GREY = '#C0C0C0'

# keep track of connected clients
client_connections = set()


def message_all(message):
    """Send a message to all active client connections.
    
    The message is formatted as JSON before sending.
    """
    for connection in client_connections:
        connection.write_message(json.dumps(message))
    print("messaged {} clients".format(len(client_connections)))


def system_message(text):
    message = json.dumps({
        "client": 'sys',
        "color": GREY,
        "message": text
    })
    for connection in client_connections:
        connection.write_message(message)
    print("system messaged {} clients".format(len(client_connections)))


def make_app():
    """Create and return the main Tornado web application.
    
    It will listen on the port assigned via `app.listen(port)`,
    and will run on Tornado's main ioloop,
    which can be started with `tornado.ioloop.IOLoop.current().start()`.
    """
    return tornado.web.Application([
        (r"/connect", ClientSocket),
        (r"/(.*)", tornado.web.StaticFileHandler, {
            "path": "client",
            "default_filename": "index.html"
        }),
    ], debug=True)


class ClientSocket(tornado.websocket.WebSocketHandler):
    """ClientSocket represents an active websocket connection to a client.
    """
    
    def open(self):
        """Called when a websocket connection is initiated."""
        
        # print some info about the opened connection
        print("WebSocket opened",
              "from user at {}".format(self.request.remote_ip))
        
        # add this connection to the set of active connections
        client_connections.add(self)
        
        # assign a random not-too-light colour
        self.color = '#'
        for i in range(3):
            self.color += hex(random.randint(0,13))[2:]
        
        # assign a nickname
        self.nickname = str(self.request.remote_ip)

    def on_message(self, message):
        """Called when a websocket client sends a message."""
        
        # print the message to the console
        print("client sent: {!r}".format(message))
        
        # try to parse the message
        try:
            parsed_message = json.loads(message)
        except ValueError:
            print("Failed to parse message: {!r}".format(message))
            return
        
        # handle the message
        self.handle_message(parsed_message)
    
    def on_close(self):
        """Called when a client connection is closed for any reason."""
        
        # print some info about the closed connection
        print("WebSocket closed",
              "by user at {}".format(self.request.remote_ip))
        print("close code: {}".format(self.close_code))
        print("close reason: {!r}".format(self.close_reason))
        
        # remove this connection from the set of active connections
        client_connections.remove(self)
    
    def handle_message(self, m):
        """Process a message from a client,
        performing any necessary actions resulting from it.
        """
        
        if m.get("message","").startswith("/nick "):
            # change nickname to match request
            original = self.nickname
            self.nickname = m["message"].split()[1]
            system_message('{} changed nickname to {}'.format(original, self.nickname))
        elif "message" in m:
            # forward the message to everyone
            message_all({
                "client" : self.nickname,
                "color" : self.color,
                "message" : m["message"]
            })
        else:
            print("message unhandled: {!r}".format(m))

if __name__ == "__main__":
    # print some basic info about the system
    print("Running Tornado Web Server {}".format(tornado.version))
    print("Using Python {}".format(sys.version))
    
    # start the webapp on port 8888
    app = make_app()
    app.listen(8888)
    print("webapp started on port 8888")
    tornado.ioloop.IOLoop.current().start()
