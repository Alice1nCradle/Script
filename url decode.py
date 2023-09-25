# coding=utf-8
import urllib
from urllib import parse

txt = input()
# URL解码
new_txt = urllib.parse.unquote(txt)
print(new_txt)
