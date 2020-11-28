"""
Zadanie 3.
wykorzystuje funkcje pomocniczą znajdująccą się poniżej, która metodą 'split'. Ilość elementów w liscie, która otrzymuję
jest o jeden większa od liczby danego znaku w stringu.
"""


import string


def counting_chars_without_ifs(filename):
  file_ref = open(filename, 'r')
  text = file_ref.read()
  spac_punc = list(string.whitespace) + list(string.punctuation)
  for sp in spac_punc:
    text = text.replace(sp,'')
  text_lower = str.lower(text)
  digits = list(text_lower)
  char_count = {}
  for digit in digits:
    char_count[digit] = find_char_number(text, digit)
    del digit
  return char_count


def find_char_number(text, digit):
  text = str.lower(text)
  temp_list = text.split(digit)
  space_number = len(temp_list) - 1
  return space_number
