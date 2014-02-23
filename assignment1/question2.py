import json
from PIL import Image

class Article:
    def _ _init_ _ (self, headline, content, author):
        self.headline = headline
        self.content = content
        self.author = author
        self.related_image = None
    def show (self):
        print "Article titled " + self.headline " written by " + self.author 
        " containing " + self.content + " with the picture " + Picture.show(self.related_image)
    def save (self):
        string = "Article titled " + self.headline " written by " + self.author 
        " containing " + self.content + " with the picture " + Picture.show(self.related_image)
        for i in range(10):
            if not os.path.exists(self.headline + i + '.txt'):
                with open(self.headline + i + '.txt', 'w') as outfile:
                    json.dump(string, outfile)
    def load_article (self, fileheader, filename, fileauthor, filepic):
        f = open(filename)
        self.headline = fileheader
        self.content = f.read()
        self.author = fileauthor
        self.related_image = filepic 

    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file

    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''

class Picture:
    def _ _init_ _ (self, filepath, title, author):
        self.filepath = filepath
        self.title = title
        self.author = author

    def show (self):
        Image.open(self.filepath)
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
