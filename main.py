import os, requests, json

bookFile = "data/Love in the Time of Cholera.txt"
searchTerm = "love"

print(os.environ)

# Get associated words
url = 'https://twinword-word-associations-v1.p.mashape.com/associations/'
headers = {
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept': 'application/json',
	'X-Mashape-Key': os.environ.get('X_MASHAPE_KEY_ASSOCIATION')
}
data = {'entry': searchTerm}
r = requests.post(url, headers=headers, data=data)

# Go through book
with open(bookName) as f:
    content = f.readlines()

for i in range(len(content)):
	paragraph = content[i].strip()
	weight = len(paragraph)



