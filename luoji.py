jixia = open ('dabaitu.txt','r')

jieguo = open ('jisuanjieguo41234.txt','w')



for i in jixia:
  jisuanyong = 0 
  canzhao = i.split()[8]

  zidian = {}
  
  
  while jisuanyong < 4 :
#    print(i.split()[jisuanyong*2])
#ge gai lv zi dian jian li  
    if i.split()[jisuanyong*2] not in zidian:
      zidian[i.split()[jisuanyong*2]] = [1,1]
      zidian[i.split()[jisuanyong*2]][0] = 1
      zidian[i.split()[jisuanyong*2]][1] = float(i.split()[jisuanyong*2+1])
    else:
      zidian[i.split()[jisuanyong*2]][0] += 1

      zidian[i.split()[jisuanyong*2]][1] +=float(i.split()[jisuanyong*2+1])
    jisuanyong += 1
  shuchu = None
  print(zidian)
  if len(zidian) == 4:
    c1 = 0
    for iwan in zidian:
      b = zidian[iwan][1]
      if b > c1 :
        c1 = b
        shuchu = iwan

  elif len(zidian) == 3:
    for ifei in zidian:
      if zidian[ifei][0] == 2:
        shuchu = ifei
  
  elif len(zidian) == 2:
    c2 = 0
    for ijian in zidian:
      b2 = zidian[ijian][1]
      if b2 > c2 :
        c2 = b2
        shuchu =ijian

  elif len(zidian) == 1:
    for gaofei in zidian:
      shuchu = gaofei

    
      
#liu xia you yong shu
#  jiheb =[i.split()[0],i.split()[2],i.split()[4],i.split()[6]]
#  c =set(b)

#  jiji = 0:
  
#  for h in c :
     
 #   while jiji < len(jiheb) :

#      if h == jiheb[jiji]:
        
#        jiheb.remove(jiheb[jiji])
#        break
        
#      jiji = jiji + 1 

#shu chu xuan ze
  
#  if len(jiheb) == 0 :
     
#    shuchu = i.split[0]

 # elif len(jiheb) == 1 :

  #  shuchu = jiheb[0]

#  elif len(jiheb) == 2 :

 #  if zidian[jiheb[0]] > zidian[jiheb[]]
     
#shu chu bi jiao 
        
  if shuchu == canzhao :

    jieguo.write(str(1)+'\n')

  else :

    jieguo.write(str(0)+'\n')
jixia.close()
jieguo.close()    
