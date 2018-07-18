from __future__ import division
import sys
import os


nage = sys.argv[1]

dakai = open(nage,'r')

suanchu = open('suanchu2.txt','w')

zhongshu = 0
zhengqueshu = 0

for i in dakai:
  
  zhongshu = zhongshu + 1
#  print(i.split()[0])

  diyi = float(i.split()[0])
  dier = float(i.split()[1])
  disan = float(i.split()[2])
  disi = float(i.split()[3])
  panduan =float(diyi)+float(dier)
  if float(panduan) > 0 :
    zhengqueshu = zhengqueshu + 1
    suanchu.write('1.0'+'\n')
  else :
    suanchu.write('0.0'+'\n')  




jieguo = round((zhengqueshu/zhongshu),7)
print(jieguo)    


dakai.close()
suanchu.close()
