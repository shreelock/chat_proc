import re
month_dict={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12};

def get_timestamp(str):
	Obj = re.search(r'(.*):(.*), (.*?) (.*)',str);
	hh=Obj.group(1).strip();
	mm=Obj.group(2).strip();
	dd=Obj.group(3).strip();
	mon=Obj.group(4).strip();
	timestamp=month_dict[mon]*1000000+int(dd)*10000+int(hh)*100+int(mm);
	return timestamp;


f=open('../wachat.txt')
chat_db=[]
entry=[]
for next in f.readlines():
	#print next.strip();
	try:
		if(next[2]==':')&(next[5]==','):
			index1 = next.index('-');
			timestring = next[0:index1];
			timestamp=get_timestamp(timestring);
			#print timestamp;
			datastring = next[index1+1:].strip();
			#print datastring;
			if((datastring.find('Shreenath:')!=-1) \
			 | (datastring.find('Tanmay Verma:')!=-1) \
			 | (datastring.find('Pratik Kumar:')!=-1) \
			 | (datastring.find('Ankita Kalra:')!=-1) \
			 | (datastring.find('Mohan Krishna:')!=-1) ):
			#for segregating between chat and Notifs
				#Matching with the regular expression of the text line;
				sObj = re.search(r'(.*): (.*)',datastring);
				print "1 = ",sObj.group(1)
				print "2 = ",sObj.group(2)
			else:
				print datastring;

			#except AttributeError: 	#The string did not match the RegEx
			#	pass				#It was probably a group notification
		else:
			print next;
	except IndexError: #The string was not a new dialogue, but it was
			pass;	   #continuation of an old one.