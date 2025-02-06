# text_processing.py
import re
import textwrap
from nltk.tokenize import word_tokenize

def clean_text_with_nltk(text):
    text = re.sub(r'[^\x20-\x7E]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\[.*?\]|\(.*?\)|\{.*?\}', '', text)
    text = re.sub(r'`+', '', text)
    tokens = word_tokenize(text)
    cleaned_text = ' '.join(tokens)
    return textwrap.fill(cleaned_text, width=80)
