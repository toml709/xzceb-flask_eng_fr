
#Final linted version of translator.py:

""" Functions implementing fr to en and en to fr translations """
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
version='2018-05-01',
authenticator=authenticator)
language_translator.set_service_url(url)

def main():
    """ Main program """
    print (english_to_french('Hello'))
    print (french_to_english("Bonjour"))

def english_to_french(english_text):
    """ en to fr translation """
    if english_text == "":
        return "Blank text - Code: 400"

    translation = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()

    return translation['translations'][0]['translation']

def french_to_english(french_text):
    """ fr to en translation """
    if french_text == "":
        return "Blank text - Code: 400"

    translation = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()

    return translation['translations'][0]['translation']

if __name__ == '__main__':
    main()
