import re
f=open('../wachat.txt')
chat_db=[]
entry=[]
#next=f.readline()
for next in f.readlines():#!= " ":
	print next
	try:
		#Matching with the regular expression of the text line;
		searchObj = re.search(r'(.*):(.*), (.*?) (.*?) (.*)',next);
		print searchObj.group(1)
		print searchObj.group(2)
		print searchObj.group(3)
		print searchObj.group(4)
		print searchObj.group(5)
	except AttributeError:
		pass
