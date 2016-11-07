#!/usr/bin/python


testDict = {'name' : 'Ganesh', 'programmer': 'yes' , 'company' : 'brocade'}
print "1.  Printing full dictinary"
print testDict
print "========================="

print "2. Looking value for key 'name'"
print testDict.get('name')
print "========================="

print "3. Adding new value"
testDict['language'] = 'python'
print testDict
print "========================="

print "4. Iterating over dictionary"
for key in testDict:
	print "Keys:" + key
	print "Values:" + testDict[key]
	print "---------------"
