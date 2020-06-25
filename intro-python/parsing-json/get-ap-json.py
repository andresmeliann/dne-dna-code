from urllib.request import Request, urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
req = Request('https://cmxlocationsandbox.cisco.com/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
response = urlopen(req)
response_string = response.read().decode('utf-8')
print(response_string)
response.close()

from json2xml import json2xml

x = {
 "pool":"http",
 "description":"My virtual server test",
 "name":"http-virtual",
 "mask":"255.255.255.255",
 "profiles":[
     {
         "name":"http",
         "kind":"ltm:virtual:profile"
     },
     {
         "name":"tcp",
         "kind":"ltm:virtual:profile"
     }
 ],
 "ipProtocol":"tcp",
 "sourceAddressTranslation":{"type":"automap"},
 "kind":"tm:ltm:virtual:virtualstate",
 "destination":"1.1.1.3:80"
}
print(json2xml.Json2xml(x).to_xml())