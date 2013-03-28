# coding: UTF-8
import urllib2
server = "http://localhost:5000/xml?query=date"
req = urllib2.Request(server)
response = urllib2.urlopen(req)
print response.read()
