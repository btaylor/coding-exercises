# Related Blogs Coding Exercise
You're a developer writing a simple blog application in Python.  You want your
blog engine to have a cool feature — each blog post will show a list of related
blog posts.  For instance, my Thanksgiving 2011 post should show my past
Thanksgiving posts.

## Related Posts (related_posts1.py):
We define related as having words in common.  The most related post is the post
with all of the same words.  Predictably, the least related post is the post
with no words in common.

The method `get_related_blog_posts` takes a BlogPost object and returns a list
of related BlogPosts sorted by the number of words in common, with the most
related post first, and the least related post last.

Please provide your first-order implementation for `get_related_blog_posts`.

## Blacklisting tokens (related_posts2.py):
Given a blacklist of common English prepositions and using the code you wrote
in `related_posts1.py`, implement `get_related_blog_posts` such that it ignores
the provided blacklisted tokens.

## Token weighting (related_posts3.py):
Tokens in the title of the blog post are often the most descriptive part of the
blog post.  Using the code from `related_posts2.py`, refine your algorithm to
weight title tokens twice as much as tokens in the body.

What is the algorithmic runtime (using O notation) of what you wrote?

## Runtime (related_posts4.py):
In this final exercise, reduce the runtime of `get_related_posts` to
O(blog.post + blog.title).  Remember that while runtime is bounded, memory is
not.
