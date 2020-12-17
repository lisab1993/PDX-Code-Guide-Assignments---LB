import requests
import string
import math

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

book = requests.get('http://www.gutenberg.org/cache/epub/1063/pg1063.txt')#everything will be lowercase, punctuaion is removed, and crate a huge list of words.
book.encoding = "utf-8"#ensure the encoding is set to utf-8
book = book.text
first_words = ("The thousand".lower())#enter the first few words of the book, and use .lower
final_words = ("End of Project Gutenberg's".lower())#enter the first words that appear at the end of the book. lower so that the program doesn't have to worry about casing issues.

book = book.lower()#convert the book to all lowercase letters.
start_of_book = book.find(first_words)#find the beginning of the actual story
end_of_book = book.find(final_words)#find the end of the actual story.
book = book[start_of_book:end_of_book]#now the book variable only contains the book. 



book = book.replace("--", " ")#replace the dashes with spaces before splitting on the whitespace
sentence_list = book.split(".")#splits the sentences into a list of strings.

book_list = book.split()#the book is a list of strings now.
for x in range(len(book_list)):#iterate over the indices within the list called book.
    book_list[x] = book_list[x].strip(string.punctuation)#at each index in the list, we will strip the punctuation from the start and end, and send it back to its index after cleanup.


monolithic_string = "".join(book_list)#this variable contains the entire book as a gigantic string. 

num_of_chars = len(monolithic_string)
num_of_words = len(book_list)#the word count is the length of the list. 
num_of_sentences = len(sentence_list)


ARI = 4.71 * (num_of_chars/num_of_words) + .5 * (num_of_words/num_of_sentences) - 21.43#math formula for the ARI
ARI = math.ceil(ARI)#always rounds up to the int above

student_age = ari_scale[ARI]["ages"]#access the nested dictionary, and add it to the variable
student_grade = ari_scale[ARI]["grade_level"]

print(f"The ARI for The Cask of Amontillado is {ARI}.")#print out the ARI, the ages it's suited for, as well as the grade level. 
print(f"This book is suitable for students aged {student_age}.")
print(f"This is appropriate for students in {student_grade}.")

