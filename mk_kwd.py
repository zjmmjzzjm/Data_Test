#encoding: utf8
import os
import re

f = open('movies.txt', 'r')
kwds = set([])
for l in f.readlines():
	sarray = re.split(',|/', l)
	for i in range(len(sarray)):
		if(i == 0):
			s1array = sarray[i].split(' ', 1 )
			for s1 in s1array:
				if s1 in kwds:
					kwds.add(s1)
		else:
			if sarray[i] not in kwds:
				kwds.add(sarray[i])

f1 = open("keywds.txt", "w")
for k in kwds:
	k1 = k.strip()
	if(len(k1) == 0):
		continue
	f1.write(k1 +"\n")

