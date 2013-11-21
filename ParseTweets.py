import sys
import json
import re

InputFile = open(sys.argv[1])


i=0
TweetDict = {}

for line in InputFile:
	Data = json.loads(line)
	statuses = Data["statuses"]
	#print Data["search_metadata"]
	name  = Data["search_metadata"]["query"]
	
	
	# print len(statuses), name
	TextList = [] 
	for i in range(len(statuses)):
		#if statuses[i]["retweeted"] == False:
		#	print statuses[i]#["retweeted"]#["text"]
		#print statuses[i]["created_at"]
		tweet = statuses[i]["text"].encode("utf-8")
		if not(tweet in TextList) and (statuses[i]["retweeted"] == False) and (statuses[i]["lang"]=="en"):
			TextList.append(tweet)
		TweetDict[name] = [TextList , statuses[i]["created_at"]]
	
#for x in TweetDict.keys():
#	print len(TweetDict[x])

print json.dumps(TweetDict)
