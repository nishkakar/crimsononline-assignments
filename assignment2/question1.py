import datetime
import re

class Content(object):
    def __init__(self, title, subtitle, creator):
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.pub_date = datetime.date.today()

    def show (self):
        print '<Title: {0}> <Subtitle: {1}> <Creator: {2}> <Publication Date: {3}>'.format(self.title, self.subtitle, self.creator, self.pub_date.__str__())

    def matches_url (self, url):
        pattern = r'http://thecrimson.com/(\w+)/(\d{4})/(\d{1,2})/(\d{1,2})/(\w+)'
        if re.search(pattern, url) is None:
            return False
        else: 
            return True

    @classmethod
    def from_url (cls, c_lst, url):
        matched_content = []
        for content in c_lst:
            sepstrings = (content.title).split()
            slug = '-'.join(sepstrings) 
            pattern = r'http://thecrimson.com/(\w+)/{0}/{1}/{2}/{3}/'.format(content.pub_date.year, content.pub_date.month, content.pub_date.day, slug)
            if re.search(pattern, url) != None: 
                matched_content.append(content)
        if len(matched_content) > 1:
            print 'Error - more than one content object matches URL'
        elif len(matched_content) == 0:
            print 'no content matched'
        else:
            return matched_content[0]    

class Article(Content):
    def __init__(self, title, subtitle, creator, related_image):
        super(Article, self).__init__(title, subtitle, creator)
        self.related_image = related_image

    def show (self):
        print '<Title: {0}> <Subtitle: {1}> <Creator: {2}> <Publication Date: {3}> <Related Image: {4}'.format(self.title, self.subtitle, self.creator, self.pub_date.__str__(), self.related_image)

class Picture(Content):
    def __init__(self, title, subtitle, creator, image_file):
        super(Article, self).__init__(title, subtitle, creator)
        self.image_file = image_file

    def show (self):
        print '<Title: {0}> <Subtitle: {1}> <Creator: {2}> <Publication Date: {3}> <Related Image: {4}'.format(self.title, self.subtitle, self.creator, self.pub_date.__str__(), self.image_file)

def posted_after(c_lst, dt):
    dt_content = []
    for content in c_lst:
        if content.pub_date < dt:
            dt_content.append(content)
    return dt_content
