#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random

class Codec:
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, long_url):
        if long_url not in self.url2code:
            code = ''.join([random.choice(self.alphabet) for _ in range(6)])
            if code not in self.code2url:
                self.code2url[code] = long_url
                self.url2code[long_url] = code
        return 'http://tinyurl.com/' + self.url2code[long_url]

    def decode(self, short_url):
        return self.code2url[short_url[-6:]]

obj = Codec()
src_url = 'https://hi.com/helloworld'
a = obj.encode(src_url)
b = obj.decode(a)
print src_url, a, b
