import datetime
import re

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

	(datetime.datetime(NewDate[0], NewDate[1],NewDate[2],NewDate[3],NewDate[4],NewDate[5]) - datetime.datetime(1970,1,1)).total_seconds()
