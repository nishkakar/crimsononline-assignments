from question1 import *
# fill in the rest!

print "==testing question1=="
print "content..."
content1 = Content('Hello', 'Whatsup', 'Me')
content1.show()
print content1.matches_url('http://thecrimson.com/article/2014/3/9/Hello')

# Content.from_url([content1], 'http://thecrimson.com/article/2014/3/9/Hello')