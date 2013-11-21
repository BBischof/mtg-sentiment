import sys
import json
import re

afinnfile = open(sys.argv[1])
tweet_file = open(sys.argv[2])
tweet_file2 = open(sys.argv[3])
tweet_file3 = open(sys.argv[4])
tweet_file4 = open(sys.argv[5])

scores = {}
lex = {}
for line in afinnfile:
	term, score  = line.split("\t")  # The file is tab-delimited. 
	scores[term] = int(score)

print len(scores.keys())

for line in tweet_file:
	dict_tweets=json.loads(line)
	tweet_words = re.findall('\w+', dict_tweets["text"])
	tweet_value = 0
	clean_word = " "
	for word in tweet_words:
		clean_word = str(word).lower()
		if clean_word not in lex.keys():
			lex[clean_word] = 0
		if clean_word in scores:
			tweet_value += scores[clean_word]
	for word in tweet_words:
		clean_word = str(word).lower()
		lex[clean_word] += tweet_value	

print len(lex.keys())

for line in tweet_file2:
	dict_tweets=json.loads(line)
	tweet_words = re.findall('\w+', dict_tweets["text"])
	tweet_value = 0
	clean_word = " "
	for word in tweet_words:
		clean_word = str(word).lower()
		if clean_word not in lex.keys():
			lex[clean_word] = 0
		if clean_word in scores:
			tweet_value += scores[clean_word]
	for word in tweet_words:
		clean_word = str(word).lower()
		lex[clean_word] += tweet_value	

print len(lex.keys())

for line in tweet_file3:
	dict_tweets=json.loads(line)
	tweet_words = re.findall('\w+', dict_tweets["text"])
	tweet_value = 0
	clean_word = " "
	for word in tweet_words:
		clean_word = str(word).lower()
		if clean_word not in lex.keys():
			lex[clean_word] = 0
		if clean_word in scores:
			tweet_value += scores[clean_word]
	for word in tweet_words:
		clean_word = str(word).lower()
		lex[clean_word] += tweet_value

print len(lex.keys())

for line in tweet_file4:
	dict_tweets=json.loads(line)
	tweet_words = re.findall('\w+', dict_tweets["text"])
	tweet_value = 0
	clean_word = " "
	for word in tweet_words:
		clean_word = str(word).lower()
		if clean_word not in lex.keys():
			lex[clean_word] = 0
		if clean_word in scores:
			tweet_value += scores[clean_word]
	for word in tweet_words:
		clean_word = str(word).lower()
		lex[clean_word] += tweet_value

print len(lex.keys())

for word in scores:
	clean_word = str(word).lower()
	if clean_word not in lex.keys():
		lex[clean_word] = 0
		lex[clean_word] += scores[clean_word]

print len(lex.keys())

#for x in lex.keys():
#	print x + "\t" + str(lex[x])# + "\n"
