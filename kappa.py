from statsmodels.stats.inter_rater import fleiss_kappa
from numpy import array
import sys

invalid_users = set([113, 123, 125, 131])

infile = open(sys.argv[1])

evals = {}

for line in infile:
    spl = line.strip().split(" | ")
    if len(spl) < 7:
        continue
    #print(spl)
    uid = int(spl[1])
    if uid in invalid_users:
        continue
    oid = spl[2]
    if oid not in evals:
        evals[oid] = {}
    eva = evals[oid]
    
    tags = spl[6].split(",")
    valid = False
    for tok in tags:
        s = tok.strip().split(":")
        if len(s) == 2:
            t = s[0]
            v = int(s[1])
            if v == 1:
                valid = True
            if t not in eva:
                eva[t] = [0, 0]
            eva[t][v] += 1
    if not valid:
        for t in eva:
            eva[t][0] -= 1

for oid, dic in evals.items():
    tab = []
    for row in dic.values():
        tab.append(row)
    t = array(tab)
    if sum(t[0]) < 2:
        continue
    #print(len(t))
    #print(t)
    print (sum(t[0]))
    #print(fleiss_kappa(t))

