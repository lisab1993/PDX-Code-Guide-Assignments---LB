import requests
import string


book = requests.get('http://www.gutenberg.org/cache/epub/1063/pg1063.txt')#everything will be lowercase, punctuaion is removed, and crate a huge list of words.
book.encoding = "utf-8"#ensure the encoding is set to utf-8
book = book.text
first_words = "the thousand"

def librarian(story,first_words):
    '''Removes the legal stuff and returns the book in lowercase letters. When your book is within a variable, enter that variable as the argument'''
    first_words = input("Please enter the first 2-3 words of the book")
    story = story.lower()#convert the book to all lowercase letters.
    start_of_story = story.find(first_words)#find the beginning of the actual story
    end_of_story = story.find("end of project")#find the end of the actual story.
    story = story[start_of_story:end_of_story]#now the book variable only contains the book. 
    return story

def num_of_chars(story):
    '''Determines the number of characters'''
book = book.replace("--", " ")#replace the dashes with spaces before splitting on the whitespace
sentence_list = book.split(".")#splits the sentences into a list of strings.

# book_list = book.split()#the book is a list of strings now.
# for x in range(len(book_list)):#iterate over the indices within the list called book.
#     book_list[x] = book_list[x].strip(string.punctuation)#at each index in the list, we will strip the punctuation from the start and end, and send it back to its index after cleanup.


# monolithic_string = "".join(book_list)#this variable contains the entire book as a gigantic string. 

# num_of_chars = len(monolithic_string)
# num_of_words = len(book_list)#the word count is the length of the list. 
# num_of_sentences = len(sentence_list)

# ARI = 4.71 * (num_of_chars / num_of_words) + .5 * (num_of_words / num_of_sentences) - 21.43

# print(ARI)

