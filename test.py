from fixed_files import Fixed_files
ff = Fixed_files('record', dic=False, checklength=False)
records = open('record.txt').readlines()
rec_in = []
for record in records:
    rec_in.append(ff.parse(record))

for rec in rec_in:
    print rec

for n, r in enumerate(rec_in):
    print ff.unparse(r) == records[n]
