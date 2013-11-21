import sys
import json
import re

InputFile = open(sys.argv[1])

for line in InputFile:
	Data = json.loads(line)
	statuses = Data["statuses"]
	#print Data["search_metadata"]	
	TextList = [] 
	for i in range(len(statuses)):
		tweet = statuses[i]
		tweet_text = tweet["text"].encode("utf-8")
		if not(tweet_text in TextList) and (tweet["retweeted"] == False) and (tweet["lang"]=="en"):
			TextList.append(tweet_text)	
			print json.dumps(tweet)


