import http.client
import urllib.request

server = "api.neople.co.kr"

apiKey = "6i2letN8a17rRTzbQcNU931YSBUoNJvK"

serverId = "cain"
encText = urllib.parse.quote("익명의갓파더")

conn = http.client.HTTPSConnection(server)
conn.request("GET", "/df/servers/" +  serverId + "/characters?characterName=" + encText + "&apikey=" + apiKey)
req = conn.getresponse()

print(req.status)
if int(req.status) == 200:
    print("Character data downloading complete!")
    stlXml = req.read()
    stlXml = stlXml.decode("utf-8")
else:
    print("OpenAPI request has been failed!! please retry")

import json

print(stlXml)

data = json.loads(stlXml)

dic = dict(data["rows"][0])

for d in dic.keys():
    print(d, ": " ,  dic[d])