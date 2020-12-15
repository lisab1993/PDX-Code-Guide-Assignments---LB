import requests
import string

book_words = {}#the words are the keys, and he counts are the values.

book = requests.get('http://www.gutenberg.org/cache/epub/1063/pg1063.txt')#everything will be lowercase, punctuaion is removed, and crate a huge list of words.
book.encoding = "utf-8"#ensure the encoding is set to utf-8
book = book.text.lower().split()#the book variable now contains the entire book with each word as it's own string in a list



for x in book:#iterate over each word in the list
    if x == string.punctuation:#check if x is a punctuation character
        book.remove[x]#remove all punctuation characters
    elif x not in book_words:#see if the word is not in the dictionary
        book_words[x] = 1#if it's not in the dict, add it with a count of 1.
    book_words[x] += 1#if the word is there, up its count by 1.




pairs = list(book_words.items())#.items returns a dictionary's key value pair as a tuple. All tuples are now within the pairs variable.
pairs.sort(key=lambda tuple: tuple[1], reverse = True)#reverse our tuples so that the key/value pairs with the highest values are now first.
for i in range(min(10, len(pairs))):#iterate over the tuples within the pairs variable. After we have the first ten tuples, we want to stop.
    print(pairs[i])#print the most common tuples based on the highest value (which is the word count.)
