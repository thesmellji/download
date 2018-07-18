




paixu = open('suanshuce23-4.txt','r')
xinjian = open('xinjiance23-4.txt','w')
a=[]

for i in paixu:
  bufen1 = i.split()[0]
  bufen2 = i.split()[1]
  bufen3 = i.split()[2]
  bufen4 = i.split()[3]
  bufen5 = i.split()[4]
  goushi = (bufen1,bufen2,bufen3,bufen4,bufen5)
  a.append(goushi) 

#for f in a:
  
#  print(f[1])
b = sorted(a,key=lambda x:x[2])
#for ff in b:
#  print(ff)

for h in b:
  fenfen1 = h[0]
  fenfen2 = h[1]
  fenfen3 = h[2]
  fenfen4 = h[3]
  fenfen5 = h[4]
  hehe= str(fenfen1) + '\t' +str(fenfen2)+'\t'+str(fenfen3)+'\t'+str(fenfen4)+'\t'+str(fenfen5)
  xinjian.write(hehe+'\n')
#xinjian.append(b)

xinjian.close
paixu.close

