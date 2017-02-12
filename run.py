import os, requests, re, json, csv

# bookFile = "app/data/Love in the Time of Cholera.txt"
bookFile = "app/data/A People's History.txt"
queryTerm = "terrorism"

# Get associated words
url = 'https://twinword-word-associations-v1.p.mashape.com/associations/'
headers = {
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept': 'application/json',
	'X-Mashape-Key': os.environ.get('X_MASHAPE_KEY_ASSOCIATION')
}
data = {'entry': queryTerm}

r = requests.post(url, headers=headers, data=data)
print(r.text)

associations = r.json()['associations_array']
associations.append(queryTerm)
associations_scored = r.json()['associations_scored']
associations_scored[queryTerm] = 3.0

	
# with open('app/data/assoc.json') as data_file:    
#     results = json.load(data_file)

# associations = results['associations_array']
# associations.append(queryTerm)
# associations_scored = results['associations_scored']
# associations_scored[queryTerm] = 3.0

# Go through book
with open(bookFile) as f:
    content = f.readlines()

delimiters = [',', '.', '?', '!', ':', ' ', '\n', '\r']

findings = []

for i in range(len(content)):
	paragraph = content[i].strip()
	if not paragraph:
		continue

	weight = len(paragraph)
	score = 0.0

	words = re.split(r'[,.?!:"“”()&*$#@ \n\r]+', paragraph)
	matched = []

	for word in words:
		word = word.strip().lower()
		if word in associations_scored:
			score += associations_scored[word]
			matched.append(word)

	findings.append({
		'paragraph': paragraph,
		'weight': weight,
		'score': score,
		'matched': matched
	})

BMIs = [[finding[attr] for attr in finding] for finding in findings]
with open('output2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(BMIs)
