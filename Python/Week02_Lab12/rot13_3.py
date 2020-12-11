import string
# Write a program that prompts the user for a string, and encodes it with ROT13. 
# For each character, find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# Index  	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j   k   l   m

# print(rot13('hello')) # uryyb



alpha = string.ascii_lowercase#our alphabet is in a string
rotated = "nopqrstuvwxyzabcdefghijklm"#don't forget that strings have indices as well.
output1 = []#make a blank list to add the rorated characters. This will be converted to a string before we return it.

user_input = input("Please enter a word to be encoded:\n>").lower()#hello
for char in user_input:#iterate over the user_input. start with the h, then e, and so on.
    x = alpha.find(char)#the x variable will hold the index of the letter.
    output1.append(rotated[x])#add the rotated character to the output1 list
output = "".join(output1)#conver the output1 list into a string
print(output)#print the string with the converted letters.

