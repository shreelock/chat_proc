import re
import matplotlib.pyplot as plt
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
message_count=0;
for next in f.readlines():
	#print next.strip();
	try:											#if the line doesn't contain more than 5 characters.
		if(next[2]==':')&(next[5]==','):			#if it is a new message that contains tiimestamp
			index1 = next.index('-');
			timestring = next[0:index1];
			timestamp=get_timestamp(timestring);
			#print timestamp;
			datastring = next[index1+1:];
			#print datastring;
			if((datastring.find('Shreenath:')!=-1) \
			 | (datastring.find('Tanmay Verma:')!=-1) \
			 | (datastring.find('Pratik Kumar:')!=-1) \
			 | (datastring.find('Ankita Kalra:')!=-1) \
			 | (datastring.find('Mohan Krishna:')!=-1) ):
			#for segregating between chat and Notifs
				#Matching with the regular expression of the text line;
				sObj = re.search(r'(.*): (.*)',datastring);
				entry=[];
				name=sObj.group(1).strip();
				msg=sObj.group(2);
				#print name, msg
				entry.append(timestamp);
				if(name=='Shreenath'):
					entry.append('S');
				elif(name=='Tanmay Verma'):
					entry.append('T');
				elif(name=='Ankita Kalra'):
					entry.append('A');
				elif(name=='Mohan Krishna'):
					entry.append('M');
				elif(name=='Pratik Kumar'):
					entry.append('P');
				entry.append(msg);
				chat_db.append(entry);
				del entry
				message_count=message_count+1;
			else:									#It was probably a group notification
				#print datastring;
				pass
				
		else:
			chat_db[message_count-1][2]=chat_db[message_count-1][2]+" "+next;		#Its not a new message
			pass

	except IndexError:								#if the line doesn't contain more than 5 characters.
			pass;	   
s=0;
t=0;
a=0;
m=0;
p=0;
k=0;
for i in xrange(0,len(chat_db)):
	if(chat_db[i][1]=='S'):
		s=s+1;
	elif(chat_db[i][1]=='T'):
		t=t+1;
	elif(chat_db[i][1]=='A'):
		a=a+1;
	elif(chat_db[i][1]=='M'):
		m=m+1;
	elif(chat_db[i][1]=='P'):
		p=p+1;
	else:
		#print chat_db[i][0];
		k=k+1;

	#print chat_db[i],"\n"
#plt.plot([0,5,10,15,20],[s,t,a,m,p]);
#plt.xlabel("S, T, A, M, P ->");
#plt.ylabel("The frequency of messaging");
#plt.show();
sp = float(s)*100/s+t+a+m+p;#len(chat_db);
tp = float(t)*100/s+t+a+m+p;#len(chat_db);
ap = float(a)*100/s+t+a+m+p;#len(chat_db);
mp = float(m)*100/s+t+a+m+p;#len(chat_db);
pp = float(p)*100/s+t+a+m+p;#len(chat_db);
#print s+t+a+m+p+k;
#print len(chat_db);
print "S = ", s;
print "T = ", t;
print "A = ", a;
print "M = ", m;
print "P = ", p;
print "STAMP = ", s+t+a+m+p;
labels = 'S', 'T', 'A', 'M', 'P'
sizes = [s, t, a, m, p]
colors = ['red', 'green', 'pink', 'skyblue', 'lightyellow']
explode = (0, 0, 0, 0,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.9f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()