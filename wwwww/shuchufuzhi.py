
from __future__ import division

import sys
import os
import commands

wenjian  = open('jieguo.txt','r')

#parser.add_argument('--wenjian','-k')

jiba = sys.argv[1]
yaokan = sys.argv[2]
shuchulei = (sys.argv[3])


zai =os.path.exists(str(jiba))
if zai == False:
  os.makedirs(str(jiba))

dashabi = open(str(jiba)+'/test.txt','w')
for i in wenjian:
  lujin = str(i.split()[0])
  shuxin = i.split()[1]
  zhengque = i.split()[2]
  if int(shuxin) == int(yaokan):
    if float(zhengque) == float(shuchulei):
      commands.getoutput('cp'+' '+lujin+' '+str(jiba))
      dashabi.write(str(lujin)+' '+str(shuxin)+'\n')  
#      yuanwenjian = open(lujin,'r')
#      savepath1 = os.path.join('shuchu/',lujin)  
#      yuanwenjian.save(savepath1)
#      yuanwenjian.close()
  if int(shuxin) > int(yaokan):
    break

dashabi.close()
wenjian.close()
#    if shuchulei == 1:
#    if shuchulei == 2:
    
