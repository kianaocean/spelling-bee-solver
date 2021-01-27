
import json
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.corpus import words

'''
Queen Bee Solver
Solves NYTimes Spelling Bee puzzle
1. Identifies today's hive letters and all valid answers from NYTimes site
2. Identifies any additional valid English words that meet requirements of puzzle
but are not valid answers because they are "obscure, hyphenated, or proper nouns"
'''


# create list of all english words in lowercase
words = [x.lower() for x in words.words()]

# scrape html from spelling bee site 
html = urlopen('https://www.nytimes.com/puzzles/spelling-bee')
soup = BeautifulSoup(html.read(), 'lxml')

# isolate relevant game data for today's puzzle, load as json
script = soup.find('script', text=re.compile('window\.gameData'))
json_text = re.search(r'{"today":{"expiration":.*$',
                      script.string, flags=re.DOTALL | re.MULTILINE).group(0)
data = json.loads(json_text)

# set variables for the center letter, outer letters, all valid letters, and all valid words
center_letter = data['today']['centerLetter']
outer_letters = data['today']['outerLetters']
valid_letters = data['today']['validLetters']
valid_answers = data['today']['answers']


# use list of all english words to find any additional words that
# satisfy rules of puzzle but are not a valid answer

# create dict with all words
pos_answers = {}
for word in words:
    pos_answers[word] = 1

for key, value in pos_answers.items():
    # check if each char in word is one of the valid letters
    for char in list(key):
        if (char not in valid_letters):
            pos_answers[key] = 0
    # check if the word is at least four characters long
    if (len(key) < 4):
        pos_answers[key] = 0
    # check to make sure the center letter is present in the word
    if (center_letter not in str(key)):
        pos_answers[key] = 0

# filter out any words that already are in list of valid answers
for key in pos_answers.keys():
    if (key in valid_answers):
        pos_answers[key] = 0

# generate new list with just the additional answers
missing_answers = []
for key, value in pos_answers.items():
    if (value==1):
        missing_answers.append(key)

# export solution to .txt file
solution = {}
solution['Center letter: '] = center_letter
solution['Outer letters: '] = outer_letters
solution['Valid answers: '] = valid_answers 
solution['Answers missing from NYTimes list: '] = missing_answers

file_out = open('queen_bee.txt', 'wt')
for key, value in solution.items():
    file_out.write(key)
    file_out.write(str(value))
    file_out.write('\n\n')
file_out.close()





