# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:43:55 2019

@author: acm-2
"""


class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def clear(self):
        self.root = Node()

    def update(self, s, val):
        now = self.root
        for c in s:
            if not c in now.next:
                now.next[c] = Node()
            now = now.next[c]
        now.value += val

    def query(self, s):
        now = self.root
        for c in s:
            if not c in now.next:
                return 0
            now = now.next[c]
        return now.value
