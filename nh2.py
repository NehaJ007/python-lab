s=raw_input("enter string")
c=0
c1=0
c2=0
c3=0
for k in s:
 if(k=='?'):
  c+=1
for k in s:
 if(k=='1' or k=='2' or k=='3' or k=='4' or k=='5'):
  c1+=1
w=s.split()
for k in w:
  c2+=1
for k in s:
 if(k=='a' or k=='e' or k=='i' or k=='o' or k=='u' or k==' '):
  continue
 else:
  c3+=1
print "?=",c
print "no=",c1
print "w=",c2
print "c=",c3
 
 
