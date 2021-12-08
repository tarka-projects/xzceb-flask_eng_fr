"""
Module to perform translations
"""
# M.Tarka IBM_4 Translator
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#authenticator = IAMAuthenticator('apikey')
authenticator = IAMAuthenticator('5HH7nbsLXcS0WxtBKCdytJu1_483Q2Yt1mqsRgE4LLap')
language_translator = LanguageTranslatorV3(version='2020-12-05', authenticator=authenticator)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """english to french function """
    translation = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text
TestEnFr=english_to_french('Sun')


def french_to_english(french_text):
    """french to english function """
    translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text