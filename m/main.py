


raw_f = open("test.txt",'r',encoding = 'utf-8')
f = str(raw_f.read())

f = f.strip().replace('\"', '\\"').replace("\'", "\\'").split("\n")
a = []
for i in f:
    a.append(str(i) + "\\n")

n = ""
for i in a:
    n = n+i


print(n)
with open('output.py', 'w') as f:
    f.write(f"exec(\"{n}\")")