import MySQLdb,urllib,urllib2,cookielib
from BeautifulSoup import BeautifulSoup

db = MySQLdb.connect("localhost","<username>","<password>","MNC")
c = db.cursor()

companies = open("MNC_List.txt","r")
comp_data = companies.read()
comp_list = comp_data.split("\n")
base_url = "http://en.wikipedia.org/wiki/"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
records=0
for company in comp_list:
	print "[+] Fetching "+company+" profile..."
	resp = opener.open(base_url+company)
	soup=BeautifulSoup(resp)
	det=soup.findAll('table',{"class":"infobox vcard"})
	name=det[0].findAll('caption',{"class":"fn org"})[0].text
	try:
		tagline=det[0].findAll('div')[0].text
	except IndexError:
		tagline = "NULL";
	industry = det[0].findAll('td',{"class":"category"})[1].text
	founded = det[0].findAll('td',{"style":"line-height:1.35em;;"})[3].text
	founders_list = det[0].findAll('li')
	founders = ""
	for i in founders_list:
		founders = founders + i.text
	headquarters = det[0].findAll('td',{"class":"adr"})#[0].text
	hq = ""
	for i in range(len(headquarters)):
		hq=hq+headquarters[i].text
	key_people = det[0].findAll('td',{"class":"agent"})#[1].text
	kp=""
	for i in range(len(key_people)):
		kp=kp+key_people[i].text
	#print kp
	services=det[0].findAll('td',{"class":"category"})#[2].text
	#print services
	ser=""
	for i in range(len(services)):
		ser=ser+services[i].text
	#print ser
	'''revenue=det[0].findAll('span',{"class":"nowrap"})#[0].text
	#print revenue
	rev = ""
	for i in range(len(revenue)):
		rev=rev+revenue[i].text
	#print rev'''
	rev=""
	website=det[0].findAll('span',{"class":"url"})#[0].text
	#print website
	ws=""
	for i in range(len(website)):
		ws=ws+website[i].text
	#print ws
	print "Name : "+name
	print "Tagline: "+tagline
	print "Industry : "+industry
	print "Founded : "+founded
	print "Founders : "+founders
	print "Hq : "+hq
	print "Keypeople"+kp
	print "Service : "+ser
	#print "Revneue : "+rev
	print "Website : "+ws
	print "[+] Inserting into database..."
	query = "INSERT INTO `Profile`(`Name`,`Tagline`,`Industry`,`Founded`,`Founders`,`Headquarters`,`Key_People`,`Services`,`Revenue`,`Website`) VALUES ('"""+name+"""', '"""+tagline+"""', '"""+industry+"""', '"""+founded+"""', '"""+founders+"""', '"""+hq+"""', '"""+kp+"""', '"""+ser+"""','"""+rev+"""', '"""+ws+"""');"""
	c.execute(query)
	db.commit()
	records+=1
	print "[+] Success... "+str(records)+ " record(s) inserted!"
	
