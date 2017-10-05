# coding: utf-8
import requests

KEY = 'API_KEY'  # this API_KEY will be disabled after the workshop


def translate_text(text, target_lang):
    response = requests.post(
        'https://translation.googleapis.com/language/translate/v2?key=' + KEY,
        data={'q': text, 'target': target_lang})

    data = response.json()
    if 'data' in data:
        return response.json()['data']['translations'][0]['translatedText']
    return text

# ---- TESTS ---------

def test_translate_to_english():
    assert translate_text("Hallo Welt", "en") == "Hello World"


def test_translate_to_german():
    assert translate_text("Hello World", "de") == "Hallo Welt"


def test_translate_error():
    assert translate_text("Hello World", "unknown") == "Hello World"
