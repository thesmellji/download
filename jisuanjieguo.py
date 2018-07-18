from __future__ import division

import sys


feiji = sys.argv[1]
wenjian = open(feiji,'r')

zhengque = 0 

zongshu = 0

for i in wenjian:
  nage = i.split()[0]
#  print(nage)
  zongshu += 1
  if nage == '1':
    zhengque  += 1

jieguo1 = round((zhengque/zongshu),7)
print(jieguo1)

wenjian.close()
