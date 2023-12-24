""" s=5
c=s
for i in range(1,s+1):
    print(" "*c+(str(i)+" ")*i+" "*c)
    c-=1
c+=2
for i in range(s-1,0,-1):
    print(" "*c+(str(i)+" ")*i+" "*c)
    c+=1
s=5
c=s+s
k=1
for i in range(s,-1,-1):
    print(" "*c+(str(i)+" ")*k+" "*c)
    c-=2
    k+=2
c=0
c+=2
k-=4
for i in range(1,s+1):
    print(" "*c+(str(i)+" ")*k+" "*c)
    c+=2
    k-=2
s=6
c=s
m=""
for i in range(1,s+1):
    m+=str(i)
    j=m[::-1]
    print(" "*c+j[:len(j)-1]+m+" "*c)
    c-=1
h=j[:len(j)-1]+m
c=0
c+=2
for i in range(1,s+1):
    print(" "*c+h[i:len(h)-i]+" "*c)
    c+=1
s=5
m=""
for i in range(s,0,-1):
    m+=str(i)
for i in range(0,s):
    print(m[:len(m)-i]+" "*2*i+m[i:])
"""
class n():
    def __init__(self,d):
        self.d=d
        self.next=None
class l():
    def __init__(self):
        self.head=None
c=""
b=l()
for i in range(1,5):
    a=n(i)
    if i==1:
        b.head=a
        c=a
    else:
        c.next=a
        c=a
i=b.head
while(i!=None):
    #print(i.d)
    i=i.next
b.head=b.head.next
i=b.head
t=""
while(i.next!=None):
    print(i)
    i=i.next
    t=i
a=n(9)
t.next=a
i=b.head
while(i!=None):
   # print(i.d)
    i=i.next
i=b.head
a=n(10)
k=4
p=""
while(i.d!=k):
    p=i
    i=i.next
p.next=i.next
#p.next.next=None
i=b.head
while(i!=None):
    print(i.d)
    i=i.next
k=1
s=5
c=s
p=1
for i in range(1,s+1):
    print(" "*c,end="")
    m=''
    for j in range(0,p):
        m+=str(k)+" "
        k+=1
    print(m," "*c)
    c-=1
    p+=2




