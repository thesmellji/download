

#wei le liang ge shu neng gou xiang chu
from __future__ import division

wenjian = open('jieguoe22-3.txt','r')
jieguo = open('suanshuze22-3.txt','w')

h=0

while h < 3755 :  
     shushu = 0
     inzhengque = 0
     
     for i in wenjian:
#          print(i) 
        panduan = i.split()[1]
#          print(panduan)
        zhengque = i.split()[2]
#          print(zhengque)
#          print(h,'loop')
#          print(int(panduan))
        if int(panduan) == h:
           shushu += 1
           inzhengque += float(zhengque)
        if int(panduan) == h+1:
           break   
#        print(h)
     zhengshu = inzhengque
     qiu = round((zhengshu/shushu),4)
     print(h)
     print(qiu)
     hangai = str(h) +' '+ str(qiu)+' '+str(zhengshu)+' '+str(shushu)
     jieguo.write(hangai+'\n')
#     print(zhengshu,'a')
#     print(shushu,'b')
#     print(qiu)
#            neng = str(qiu)
#	jieguo.write(neng+'\n')
#            break
     h += 1
#        continue        

wenjian.close()
jieguo.close()
