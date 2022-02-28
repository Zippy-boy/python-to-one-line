import os
import argparse
from pathlib import Path
parser = argparse.ArgumentParser()

parser.add_argument('first', type=str, help="Full path to file")
parser.add_argument('-o', '--output', type=str, help="The outputed file", required=False)

args = parser.parse_args()
raw_f = open(args.first,'r',encoding = 'utf-8')
f = str(raw_f.read())
f = f.strip().replace("\t", "\\t").replace("\\", "\\\\").replace('\"', '\\"').replace("\'", "\\'").split("\n")
a = []
for i in f:
    a.append(str(i) + "\\n")
n = ""
for i in a:
    n = n+i

input_path = args.first
output_path = args.output
output_path_none = args.first

o = output_path_none.split("\\")
print(o)
o.pop()
output_path_none = ""
for i in o:
    output_path_none = output_path_none+i+"\\"
print(output_path_none)



#print(n)

if output_path == None:
    with open(output_path_none + "output.py", 'w') as f:
        f.write(f"exec(\"{n}\")")

else:
    with open(f"{output_path}\\output.py", 'w') as f:
        f.write(f"exec(\"{n}\")")
    print("hi")
