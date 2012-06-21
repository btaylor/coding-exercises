#!/usr/bin/python
# -*- coding: utf-8 -*-

# ## Related Posts (related_posts1.py):
# We define related as having words in common.  The most related post is the
# post with all of the same words.  Predictably, the least related post is the
# post with no words in common.
# 
# The method `get_related_blog_posts` takes a BlogPost object and returns a list
# of related BlogPosts sorted by the number of words in common, with the most
# related post first, and the least related post last.
# 
# Please provide your first-order implementation for `get_related_blog_posts`.

from models import BlogPost

posts = []
def import_blog_posts():
    for i in xrange(0, 8):
        lines = open('posts/%d.txt' % i).readlines()
        posts.append(BlogPost(lines[0], ''.join(lines[1:])))

def tokenize_blog_post(b):
    return b.body.lower().split(' ') + b.title.lower().split(' ')

def get_related_blog_posts(b):
    return []


if __name__ == "__main__":
    import_blog_posts()
    print get_related_blog_posts(BlogPost('Symbolic Icons',
"""
GNOME 3 introduced a new style of icons we call symbolic. Last year, Meg Ford
joined the effort we kicked off with Lapo and did a great job extending the
theme coverage, without us having any style guidelines in place yet. This year,
we’ll have another Woman Outreach program participant joining the effort, so
I’ve edited a little video introduction on how we design these icons along with
a little overview of all the icon styles currently in place.
"""))
