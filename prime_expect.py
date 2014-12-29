import pexpect,commands
def sqrt(n):
  """ Efficient sqrt Algorithm """
  x = n
  y = (x + n / x) / 2
  while y < x:
    x = y
    y = (x + n / x) / 2
  return x
def isPrime(num):
    """ Primality Test Algorithm """
    if num<=1:
        return 0
    if num==2:
        return 1
    if num%2 == 0:
        return 0
    sRoot = sqrt(num*1.0)
    i=3
    while(i<=sRoot):
        if(num%i==0):
            return 0
	i+=2
    return 1
c=pexpect.spawn("nc 128.199.215.224 8080")
c.expect("(exclusive)")
a=int(c.before.split("\n")[3])
b=int(c.before.split("\n")[5])
while(a<b):
	if(isPrime(a)):
		out=a
		break
	a+=1
c.sendline(out)
c.interact()
