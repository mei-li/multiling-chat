[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Presentation
https://docs.google.com/presentation/d/14fNHXKKIBnz0icLOQummEuuKk-YazkqYkC6RkmooZdA/edit?usp=sharing

Multilingual chat application
=============================
This is a application and workshop/exercise to extend a chat application with Tornado to tranlate user messages.

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

Go inside `step0` directory. Check in `translate.py` file. Add the correct key in the `API_KEY` variable.
Complete `translate_text` function code, by calling translate API so that this function translates the given 
`text` to the `target_lang`. 
Use `requests` library, `POST` method to call Google translate API endpoint. NO NEED to use the python library. 
For authentication use the query parameter `key=API_KEY`, aka add `?key-API_KEY` after the url. Run tests to check correctness.

Test:

    py.test translate.py

Resources:
    
   - Translate API docs: https://cloud.google.com/translate/docs/translating-text
   - requests library docs (POST method): http://docs.python-requests.org/en/master/user/quickstart/#make-a-request


Step 1: Set language command 
----------------------------
Go to step1 directory. In `server.py` edit `handle_message` method to add a 
new `/lang <language_code>`. Store the `<language_code>` in an attribute called `lang` inside `ClientSocket` object.

Tip:
    Add a call to `system_message` to show the language change to all connections/users.

Run server: (run server and test manually)
    
    python server.py
    # navigate to localhost:8888 in the browser


Step 2: Translate to user language 
----------------------------------
Go to step2 directory. Replace the correct `API_KEY` in `translate.py`. Now open `server.py` and edit `message_all` to 
translate the text to each connection language before sending it. Use `translate_text` function that is already imported.


The end
-------
Yei!! you should have a multilingual chat application running now, like in `final` directory. 

    cd final
    TRANSLATE_API_TOKEN=... python server.py

If you want more you can look at the extra steps or checkout the original application of last 
PyLadies workshop (by Thomas Iorns) that is the base code of this session and supports additionally 
shared drawing!! (connect two users and then click in the white area of the page to draw)

    git clone https://github.com/mesilliac/multitude.git


Extras
------
* Make sure the language that the user sets is valid, check https://cloud.google.com/translate/docs/discovering-supported-languages (tip: call the API only once)
* Sent also the original/untranslated text to all users as a command_message
* Click on deploy to heroku button on top to deploy a cloud version of the application



Next steps
----------
* get your own API_KEY or service account key and try to connect it with another google API, eg. speech to text, to 
get multilingual autosubtitle talks (speech to text chnarges by hour) or connect to Natural Language API to get user mood 
when chating. Or go to a gaming direction by enhancing its javascript (like in the original app by Thomas, https://github.com/mesilliac/multitude.git)
