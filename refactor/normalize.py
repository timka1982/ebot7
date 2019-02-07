#!/usr/local/bin/python3
# coding: utf-8

import string
import numpy as np
import re
import nltk

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
de_numbers = ['null', 'eins', 'zwei', 'drei', 'vier', 'fuenf', 'sechs', 'sieben', 'acht', 'neun']
de_digit_map = dict(zip(
    (ord(d) for d in digits),
    (' '+num+' ' for num in de_numbers)
    ))

en_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
en_digit_map = dict(zip(
    (ord(d) for d in digits),
    (' '+num+' ' for num in en_numbers)
    ))

fr_numbers = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
fr_digit_map = dict(zip(
    (ord(d) for d in digits),
    (' '+num+' ' for num in fr_numbers)
    ))

nl_numbers = ['nul','een','twee','drie','vier','vijf','zes','zeven','acht','negen']
nl_digit_map = dict(zip(
    (ord(d) for d in digits),
    (' '+num+' ' for num in nl_numbers)
    ))


digit_maps = {'en' : en_digit_map, 'de':de_digit_map, 'fr': fr_digit_map, 'nl' : nl_digit_map }

def digit_to_number(text, lang='de'):
    return text.translate(digit_maps[lang])

punctuation = '-§!&"«»“”‘’„#$€%\'()*+,./:;<=>?@[\\]^_`{|}~'
remove_punctuation_map = dict((ord(char), None) for char in punctuation)

url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
single_char_regex = "\s\w\s"

def remove_punctuation(text):
    return text.translate(remove_punctuation_map)

def remove_urls(text):
    return re.sub(url_regex, '', text)

def remove_single_chars(text):
    return re.sub(single_char_regex, '', text)

def normalize(text, lang='de'):
    text = remove_urls(text)
    text = remove_punctuation(text)
    text = remove_single_chars(text)
    text = text.lower()
    text = text.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    text = text.replace('ß', 'ss')
    text = text.replace('é', 'e').replace('è', 'e').replace('ê', 'e')
    text = text.replace('á', 'a').replace('à', 'a').replace('ê', 'e')
    text = digit_to_number(text, lang)
    text = re.sub(r'[^a-z]+', ' ', text)
    return text.strip()
