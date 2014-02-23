"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""

def common_words(filename):
    f = open(filename)
    dict = {}
    word = ''
    for c in f.read():
        if c.isspace():
            if word in dict:
                dict[word] += 1
                word = ''
            else: 
                dict[word] = 1
                word = ''
        else: 
            word = word + c
    print [pair[0] for pair in sorted(dict.items(), key = lambda item: item[1], reverse = True)]
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
#common_words("words.txt")

def common_words_min(filename, min_chars):
    f = open(filename)
    dict = {}
    word = ''
    for c in f.read():
        if c.isspace():
            if len(word) >= min_chars:
                if word in dict:
                    dict[word] += 1
                    word = ''
                else: 
                    dict[word] = 1
                    word = ''
            else:
                word = ''
        else: 
            word = word + c
    print [pair[0] for pair in sorted(dict.items(), key = lambda item: item[1], reverse = True)]
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
#common_words_min("words.txt", 6)
    

def common_words_tuple(filename, min_chars):
    f = open(filename)
    dict = {}
    word = ''
    for c in f.read():
        if c.isspace():
            if len(word) >= min_chars:
                if word in dict:
                    dict[word] += 1
                    word = ''
                else: 
                    dict[word] = 1
                    word = ''
            else:
                word = ''
        else: 
            word = word + c
    print sorted(dict.items(), key = lambda item: item[1], reverse = True)
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
#common_words_tuple ("words.txt", 7)

def common_words_safe(filename, min_chars):
    try:
        f = open(filename)
        dict = {}
        word = ''
        for c in f.read():
            if c.isspace():
                if len(word) >= min_chars:
                    if word in dict:
                        dict[word] += 1
                        word = ''
                    else: 
                        dict[word] = 1
                        word = ''
                else:
                    word = ''
            else: 
                word = word + c
        print [pair[0] for pair in sorted(dict.items(), key = lambda item: item[1], reverse = True)]
    except IOError:
        print 'File Missing!'
    finally: 
        print 'All Done!'
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
# common_words_safe ("words.txt", 7)