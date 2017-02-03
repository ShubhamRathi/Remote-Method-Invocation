# saved as client.py
import Pyro4
kerberos = Pyro4.Proxy("PYRONAME:example.kerb")    # use name server object lookup uri shortcut

name = raw_input("What is your name? ").strip()
print(kerberos.get_fortune(name))

a,b = raw_input("Enter 'a', 'b' to get it sum ").split(' ')
print(kerberos.sum(a,b))

print ("Files under Server\n")
print(kerberos.listdir())

fname = raw_input("Enter filename to transfer ").strip()
x = kerberos.sendfile(fname)
if (x):
	f = open('./Client/'+str(fname), 'w')
	print >> f, kerberos.sendfile(fname)
	f.close()
else:
	print "File not found"