from bs4 import BeautifulSoup

soup = BeautifulSoup(open("/home/vijay/PAS/page"))

#print(soup.prettify())
with open("/home/vijay/PAS/updates") as f:
	old=f.readline()


update=""
for row in soup.find_all('div',attrs={"class" : "notice-element"}):
	con=row.text
	content=con.split('\n')
	tail=""
	flag=0
	for line in content:
		if not len(line)==0:
			if flag==0:
				head= line
				flag=1
			elif flag==1:
				flag=2

			elif flag==2:
				tail=tail+"\n"+line
#	print head,tail
	update=update+head+"\n"

	if not head==old[:-1]:
		print head
	else: break

f = open('/home/vijay/PAS/updates', 'w')
f.write(update)

	
