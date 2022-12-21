import xmltodict, json
import time

start_point = time.time()

with open("tt.xml", "r") as file:
    xml = file.readlines()

data = "".join(xml)
xpars = xmltodict.parse(data)
json = json.dumps(xpars)
#print(json) 

wr = open("tt.json","w")
wr.write(json)

end_point = time.time()

print(f"Время выполнения: {end_point - start_point}")