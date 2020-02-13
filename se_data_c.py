import heap
import re

myheap = heap.heap(300)

class cell():
	def __init__(self):
		self.ch = None
		self.rc = None
		self.lc = None
		self.val = 0

l = []
d = {}

def analyze(fn):
	with open(fn,'r') as f:
		for line in f:
			for char in line:
				if char in l:
					d[char] = d[char] + 1
				else:
					l.append(char)
					d[char] = 1
	return 0
	
analyze("one.txt")
print l
print d

def sorting(l):
	for i in range(len(l)):
		for j in range(len(l)):
			if l[i].val < l[j].val:
				temp = l[j]
				l[j] = l[i]
				l[i] = temp
	return 0

ln = []

for k in d:
	ln.append([k,d[k]])
	
print ln

def makeCell(c):
	nodeAddr = myheap.malloc()
	node = cell()
	node.ch = c
	myheap.set_cell(nodeAddr,node)
	return node

nl = []
	
def makeList(c):
	for i in ln:
		nnode = makeCell(i[0])
		print nnode.ch
		nnodeAddr = myheap.malloc()
		nnode.val = i[1]
		myheap.set_cell(nnodeAddr,nnode)
		nl.append(nnode)

makeList(ln)
#sorting(nl)
#print len(nl)		
#for i in nl:
#	print "--value -- ",i.val,"-- char --",i.ch
	
def makeTree(l):
	while(len(l)>1):
		sorting(l)
		nn0 = cell()
		nn0Addr = myheap.malloc()
		nn0.val = l[0].val + l[1].val
		nn0.ch = "-node-"
		if l[0].val < l[1]:
			nn0.rc = l[0]
			nn0.lc = l[1]
		else:
			nn0.rc = l[1]
			nn0.lc = l[0]
		myheap.set_cell(nn0Addr,nn0)
		l[0] = nn0
		l.remove(l[1])
	return l[0]
	
tnode = makeTree(nl)

def preOrder(n):
    node = n
    print(node.ch)
    if node.lc != None:
        preOrder(node.lc)
    if node.rc != None:
        preOrder(node.rc)

preOrder(tnode)


s = []
coded_l = []

def encode(node,code):
    c1=node.lc
    c2=node.rc
    if(c1!=None):
        code.append(0)
        encode(node.lc,code)
    if(c2!=None):   
         code[len(code)-1]=1
         encode(node.rc,code)
         code.pop()
    else:
        l2=''
        code=code
        l1=node.ch
        for i in range(len(code)):
            l2+=str(code[i])
        
        coded_l.append([l1,l2])

encode(tnode,s)
print coded_l
	
