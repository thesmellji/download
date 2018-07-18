import pylab
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("result")
args = parser.parse_args()

txs = []
vxs = []
tys = []
vys = []
for line in open(args.result):
    print line
    data = json.loads(line)
    if data["type"] == "val":
	    vxs.append(data["iteration"])
	    vys.append(data["error"])
    else:
	    txs.append(data["iteration"])
	    tys.append(data["error"])
pylab.xlabel("iteration")
pylab.ylabel("error")
pylab.plot(txs, tys)
pylab.plot(vxs, vys)
pylab.show()
