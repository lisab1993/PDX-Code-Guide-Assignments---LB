import requests


response = requests.get("https://adventofcode.com/2020/day/1/input")
response = response.text


print(response)