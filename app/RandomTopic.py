#coding: utf8

import urllib.request

def get_random_title():
   response = urllib.request.urlopen('http://en.wikipedia.org/wiki/Special:Random')
   html = response.read()

   html = repr(html)
   i = html.find('<title>')
   j = html.find('</title>')
   return html[i+len('<title>'):j-len(' - Wikipedia, the free encyclopedia')]

def get_random_topic():
   t = get_random_title()
   while '\\' in t or ', ' in t: ## so neither escape char.s nor city names
      t = get_random_title()
   return t

'''
print(get_random_topic())
print(get_random_topic())
print(get_random_topic())
print(get_random_topic())
print(get_random_topic())
print(get_random_topic())
print(get_random_topic())
print(get_random_topic())

'''
