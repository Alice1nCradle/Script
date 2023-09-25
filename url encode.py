# coding=utf-8
import urllib
from urllib import parse

txt = input()
# URL解码
new_txt = urllib.parse.quote(txt)
print(new_txt)