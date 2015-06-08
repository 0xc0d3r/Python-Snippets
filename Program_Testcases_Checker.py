import pexpect,os,sys
home = os.environ['HOME']
src_dir = os.getcwd()+"/run/"
out_dir = os.getcwd()+"/output/"
files = os.listdir(src_dir)
inp = open(sys.argv[1],"r").readlines()
out = open(sys.argv[2],"r").readlines()
os.chdir(src_dir)
for file in files:
	ctc = 0
	os.system("gcc "+file+" -lm")
	print("\n[+] Executing "+file+" ...")
	output = open(out_dir+file[:-1]+"output","a")
	for i in range(len(inp)):
		c = pexpect.spawn("./a.out")
		c.send(inp[i].strip()+"\r\n")
		c.expect(".*")
		cout = c.readlines()
		if cout[2].strip() == out[i].strip():
			msg = "TC #%d is correct"%(i+1)
			print msg
			ctc+=1
			output.write(msg+"\n")
		else:
			msg = "TC #%d is wrong"%(i+1)
			print msg
			output.write(msg+"\n")
	os.system("rm a.out")
	print "\n[+] "+file+" completed (%d/%d) test cases."%(ctc,len(inp))
