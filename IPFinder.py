import requests
import json 


get = requests.get("https://www.ipinfo.io")
dic = get.json()
del(dic['readme'])
for each in dic.keys():
	print(each,':',dic[each])

