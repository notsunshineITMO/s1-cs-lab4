import re
import time

start_point = time.time()

with open("tt.xml", "r") as file:
    xml = file.readlines()
xml = [i.replace("\n","") for i in xml]
#print(xml)

def simple_lines(s):
    l = s.split()
    return f'\"{l[0][1:-1]}\"' +": " + f'\"{l[1][:l[1].index("<")]}\"'

res = ["{"]
"[MODIFY] rename 2 variables"

for line in xml:
    if re.fullmatch(r'<\w*>', line) != None:
        res.append(f'\"{line[1:-1]}\": {"{"}')
    
    if re.fullmatch(r'<\w*> \S*', line) != None and len(re.findall(r'<\S*>', line)) == 1:
        res.append(f'\"{line.split()[0][1:-1]}\": {"{"}')
        res.append(f'\"#text\": \"{line.split()[1]}\"')

    if re.fullmatch(r'<\w*> \S*', line) != None and len(re.findall(r'<\S*>', line)) == 2:
        res.append(simple_lines(line)) 

    if re.fullmatch(r'</\S*>', line):
        res.append("}")

for i in range(len(res) - 1):
    if res[i + 1] != "}" and "{" not in res[i]:
        res[i] += ","

res.append("}")
#print("\n".join(res))
wr = open("tt.json","w")
wr.write("\n".join(res))

end_point = time.time()
print(f"Время выполнения: {end_point - start_point}")