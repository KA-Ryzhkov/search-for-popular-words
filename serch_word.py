import io
import re

exception = []  # Exception words
letters = 5  # The minimum number of letters in a word
file = 'text.txt'

"""

Searches for the most popular word in the text and displays it indicating how many times it appears in the text.

If there are several popular words, it displays the lexicographically first.

"""

text = ''
with io.open(file, encoding='utf-8') as f:
    for i in f:
        text += i.strip()
        text = re.sub('[.,)(!@#$123456789]', '', text)  # Delete unnecessary characters
text = text.lower().split()
popularity_dic = {}  # Accumulates, how much each word appears in the text
for i in text:
    if i in popularity_dic:
        continue
    popularity_dic[i] = 0
    for j in text:
        if i == j:
            popularity_dic[i] += 1
result = ''
counter = 0
for i in popularity_dic:
    if len(i) < letters or i in exception:
        continue
    elif popularity_dic[i] > counter:
        result = i
        counter = popularity_dic[i]
    elif popularity_dic[i] == counter and i > result:
        result = i
        counter = popularity_dic[i]

print('Most popular word:', result)
print('Met:', counter, 'times')
