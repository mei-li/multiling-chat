Multilingual chat application
=============================
This is a application and workshop/exercise to extend a chat application with Tornado to tranlate user messages.

Note: The API key in the code examples exercise is not valid, create you own in google cloud platform
(google cloud translate API has to be enabled as well).

Environment setup
-----------------
Clone the repository

    git clone https://github.com/mei-li/multiling-chat.git

Python 3.5+ is required. Also install the requirements with:

`pip install -r requirements.txt`

Make sure the application runs:

    cd step0/
    python server.py

navigate in `localhost:8889` in the browser. Try the app (add text in the box,
try the `/nick <yournickname>` command, open another window - not tab and do the same)


Hands on session.
-----------------
It is a self-paced hands on session. Work alone or in a group. Each step has an exercise. Every step is
relevant to te corresponding directory. Try to implement each step, or move to the next step directory
that includes an implementation of the step.

For beginners: Insist on the step 0, it is independent and has a test to help develop.


Step 0: Translate function
--------------------------

Go inside `step0` directory. Implement `translate_text` function in `translate.py`. Use translate API so that this function translates 
the given `text` to the `target_lang`. For authentication use the query parameter `key-API_KEY`, aka
add `?key-API_KEY` after the url. 

Resources:
    Translate API docs: https://cloud.google.com/translate/docs/translating-text
    requests library docs (POST method): http://docs.python-requests.org/en/master/user/quickstart/#make-a-request

Test:

    py.test translate.py


Step 1: Set language command 
----------------------------
In `server.py` edit `handle_message` method to add a 
new `/lang <language_code>`. Store the `<language_code>` in an attribute inside `ClientSocket` object.

Tip:
    Add a `system_message` to show the language change to all connections/users.


Step 2: Translate to user language 
----------------------------------
In `server.py` edit `message_all` to translate the text to each user language before sending it. 
Use `translate_text` function from step1.


The end
-------
Yei!! you should have a multilingual chat application running now, like in `final` directory. 
If you want more you can look at the extra steps or checkout the original application of last 
PyLadies workshop (by Thomas Iorns) that is base code of this session and supports additionally 
shared drawing!! (connect two users and then click in the white area of the page to draw)

    git clone https://github.com/mesilliac/multitude.git


Extras
------
* Make sure the language that the user sets is valid, check https://cloud.google.com/translate/docs/discovering-supported-languages (tip: call the API only once)
* Sent also the original/untranslated text to all users as a command_message


For home
--------
* get your own API_KEY or service account key and try to connect it with another google API, eg. speech to text, to 
get multilingual autosubtitle talks (speech to text chnarges by hour) or connect to Natural Language API to get user mood 
when chating. Or go to a gaming direction by enhancing its javascript (like in the original app by Thomas, https://github.com/mesilliac/multitude.git)
