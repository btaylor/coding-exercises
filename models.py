#!/usr/bin/python
# -*- coding: utf-8 -*-

class BlogPost:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __unicode__(self):
        return "%s: %s..." % (self.title, self.body[:25].replace('\n', ' '))

    def __repr__(self):
        return self.__unicode__()
