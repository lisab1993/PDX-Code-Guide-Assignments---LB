
import requests
import json

user_tag = input("Please enter a keyword for your quote \n>").lower().strip()#ask the user for their keyword

loop_control = "yes"
question = "yes"

user_page = 1
while loop_control == "yes":

    if question == "yes":
        user_page += 1
        print(user_page)
    else:
        exit()
            
    response = requests.get("https://favqs.com/api/quotes/?", params={ "page":user_page, "filter":user_tag}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},)#the url gets a random quote from the Internet, which is contained within the page variable
    response = response.json()#convert our url into a json file
    quotes = response["quotes"]#search through the json file, and find the list called quotes. Place it in its own variable.

    for i in range(len(quotes)):#iterate through the list called quotes.
        print(len(quotes))
        list_items = quotes[i]#quotes of i are the list items. They are integers in the actual data.
        list_items = (quotes[i]['body'])#finds the key called "body", and puts its value in a variable.
        author = (quotes[i]["author"])#find the "author" key
        print()#place a blank space between quotes for readibility.
        quote_and_author = (list_items + " - " + author)#prints the quote and the author.
        print(quote_and_author)
    question = input("Would you like to see the next page? \n>")#after printing out the first page, ask the user if they want to see the next one.
    





