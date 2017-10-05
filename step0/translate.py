# coding: utf-8
import requests


def translate_text(text, target_lang):
    return text

# ---- TESTS ---------

def test_translate_to_english():
    assert translate_text("Hallo Welt", "en") == "Hello World"


def test_translate_to_german():
    assert translate_text("Hello World", "de") == "Hallo Welt"


def test_translate_error():
    assert translate_text("Hello World", "unknown") == "Hello World"