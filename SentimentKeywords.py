import sys
import json
import re
import datetime

afinnfile = open(sys.argv[1])
tweet_file = open(sys.argv[2])

scores = {}
keywords = {}
keywords_lists = {}
for line in afinnfile:
	term, score  = line.split("\t")  # The file is tab-delimited. 
	scores[term] = int(score)

#a function which converts the weird twitter format time to epoch time 

def TwitterTime(input):

	Months = {}
	Months["Jan"] = 1
	Months["Feb"] = 2
	Months["Mar"] = 3
	Months["Apr"] = 4
	Months["May"] = 5
	Months["Jun"] = 6
	Months["Jul"] = 7
	Months["Aug"] = 8
	Months["Sep"] = 9
	Months["Oct"] = 10
	Months["Nov"] = 11
	Months["Dec"] = 12

	Date = re.findall('\w+', input)
	NewDate = [int(Date[7]) , int(Months[Date[1]]) ,int(Date[2]) , int(Date[3]) ,int(Date[4]) ,int(Date[5])]

	return (datetime.datetime(NewDate[0], NewDate[1], NewDate[2], NewDate[3], NewDate[4], NewDate[5]) - datetime.datetime(1970,1,1)).total_seconds()

#read the dictionary of tweets associated to a keyword, do term sentiment analysis	

for line in tweet_file:
	dict_tweets=json.loads(line)
#	print dict_tweets.keys()
	for card in dict_tweets.keys():
		keywords[card] = 0
		keywords_lists[card] = []
		keyword_value = 0
		keyword_values = []
		for i in range(len(dict_tweets[card][0])):
			tweet_words = re.findall('\w+', re.sub("\'", "", re.sub("\"", "", dict_tweets[card][0][i])))
			tweet_value = 0
			clean_word = " "
			for word in tweet_words:
				clean_word = str(word).lower()
				if clean_word in scores:
					tweet_value += scores[clean_word]
			keyword_values.append([dict_tweets[card][0][i], tweet_value, TwitterTime(dict_tweets[card][1])])
			keyword_value += tweet_value
		if len(dict_tweets[card]) > 0:	
			keywords_lists[card] = keyword_values
			keywords[card] = keyword_value / len(dict_tweets[card])

# print keywords
#print keywords_lists 


sorted_list = []
#new_list = []
new_dict = {}
print keywords_lists.keys()
for card in keywords_lists.keys():
	print card		
	print len(keywords_lists[card])
	string_list = []
	coord_list = []
	for i in range(len(keywords_lists[card])):
#		new_list.append([int(keywords_lists[card][i][2]), int(keywords_lists[card][i][1]), keywords_lists[card][i][0].encode("utf-8")])
#		print "{ x: " + str(keywords_lists[card][i][2]) + ", y:" + str(keywords_lists[card][i][1]) + " }," 
#		print keywords_lists[card][i][2]

		string_list.append("StringData[\"" + str(keywords_lists[card][i][2] + ((i+1) / float(100))) + "#" + str(keywords_lists[card][i][1] + 25) + "\"] = \"" + re.sub("\'", "", re.sub("\"", "", keywords_lists[card][i][0])) + "\";")		
		coord_list.append("{ x: " + str(keywords_lists[card][i][2] + ((i+1) / float(100))) + ", y:" + str(keywords_lists[card][i][1] +25 ) + " },")
#		sorted_list = sorted(new_list, key=lambda x: x[0])
#		new_dict[card] = sorted_list
	for j in range(len(string_list)):
		print string_list[j].encode("utf-8")
	print "var Data = [ "
	for k in range(len(coord_list)):
		print coord_list[k]
	print "];"

#line = re.sub('[!@#$]', '', line)


#print new_dict.keys()
#for j in range(len(sorted_list)):
#	print "{ x: " + str(sorted_list[j][0]) + ", y:" + str(sorted_list[j][1]) + " },"

#for card in new_dict.keys():
#	print card
#	print len(new_dict[card])
#	for j in range(len(new_dict[card])):
#		print "StringData[" + str(sorted_list[j][0]) + "#" + str(sorted_list[j][1]) + "] = \"" + str(sorted_list[j][2]) + "\";"
