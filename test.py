cd ..
cd File-Fixed/
from fixed_files import Fixed_files
fj = r'C:\BNB\S303\GERADOS\Json\B303W80.json'
ff = Fixed_files(fj, dic=True, checklength=False)
rt = r'C:\BNB\S303\GERADOS\Json\B303W80.txt'
records = open(rt).readlines()
rec_in = []
for record in records:
    rec_in.append(ff.parse(record))
rec_in
for rec in rec_in:
    print rec

for n, r in enumerate(rec_in):
    print ff.unparse(r) == records[n]
