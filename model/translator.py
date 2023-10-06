from google.cloud import translate_v2 as translate
import os


class Translator:
    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'model/google_translate_api_key.json'
        self.client = translate.Client()
        self.valid_languages = ['en', 'ar', 'fa', 'ur', 'zh-CN', 'zh-TW', 'ru', 'hi']

    def translate_text(self, text, tgt_language="en"):
        result = self.client.translate(text, target_language=tgt_language)
        return result["translatedText"]
        # return "rent a villa of 4 bedrooms for less than 6 months"
