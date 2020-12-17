
import requests
import json


#comes in as a string
#take the json, use it's syntax, and make it a python dictionary. 
#json.loads(string)
#once it becomes a python dictionary, you're home free.

response = requests.get("https://favqs.com/api/qotd")#the url gets a random quote from the Internet, which is contained within the page variable
response_data = json.loads(response.text)#gets us the json of the url. 
# print(response_data)

# tags = input("What would you like your quote to be about? \n>")

find_author = response_data["quote"]["author"]#just like in a python dictionary within a dictionary, access the json file in a similar manner. 
# print(find_author)
find_quote = response_data["quote"]["body"]#do the same for the quote. When I looked in the json file, it was called the body.
# print(find_quote)
output = (f"{find_quote} - {find_author}.")
print(output)