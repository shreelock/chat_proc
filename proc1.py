import re
f=open('wachat.txt')
chat_db=[]
entry=[]
next=f.readline()
index1 = next.index('-');
print index1
timestamp = next[0:index1];
print timestamp

#while next!=" ":
#	print next
#	next=f.readline()
#for month in f.readlines():
#	print(month.strip())