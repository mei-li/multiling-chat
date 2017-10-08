# coding: utf-8
import requests
import os


def translate_text(text, target_lang):
    KEY = os.getenv('TRANSLATE_API_TOKEN', 'FAKE_TOKEN')
    response = requests.post(
        'https://translation.googleapis.com/language/translate/v2?key=' + KEY,
        data={'q': text, 'target': target_lang})

    data = response.json()
    if 'data' in data:
        return response.json()['data']['translations'][0]['translatedText']
    # in case the API Key is not filled
    if data.get('error') and 'API key not valid' in data['error']['message']:
        raise Exception("APIKey Invalid, please add the correct key!")
    return text


def test_translate_to_english():
    assert translate_text("Hallo Welt", "en") == "Hello World"


def test_translate_to_german():
    assert translate_text("Hello World", "de") == "Hallo Welt"


def test_translate_error():
    assert translate_text("Hello World", "unknown") == "Hello World"
