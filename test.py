import re

testStr = '244.99"'

r1 = re.findall("[0-9]+.[0-9]+", testStr)
print(r1)