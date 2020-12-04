import pickle
import json
from tqdm import tqdm
import glob2
import codecs
import csv
import re
import sys
import random
import string
import re

# https://realpython.com/python-encodings-guide/
# List of available words with mark in Vietnamese

intab_l = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
whitespace = ' '
accept_strings =  intab_l + ascii_lowercase + digits + punctuation + whitespace
r = re.compile('^[' + accept_strings + ']+$')

#Check Vietnamese function :
def _check_tieng_viet(seq):
  if re.match(r, seq.lower()):
    return True
  else:
    return False
# _check_tieng_viet('tiếng việt thần thánh cực kỳ')

# Remove tone Function : 
def remove_tone_line(utf8_str):
    intab_l = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"
    intab_u = "ẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ"
    intab = list(intab_l+intab_u)

    outtab_l = "a"*17 + "o"*17 + "e"*11 + "u"*11 + "i"*5 + "y"*5 + "d"
    outtab_u = "A"*17 + "O"*17 + "E"*11 + "U"*11 + "I"*5 + "Y"*5 + "D"
    outtab = outtab_l + outtab_u
    # Using regex to find out the order of alphabe has tone like this 'ạ|ả|ã|...'
    r = re.compile("|".join(intab))

    # Dictionary replace them from tone to untone. VD: {'â' : 'a'}
    replaces_dict = dict(zip(intab, outtab))
    # Replace all of them by regex through the order of it
    non_dia_str = r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)
    return non_dia_str
  
# remove_tone_line('Đi một ngày đàng học 1 sàng khôn')



