import re
txt="The ra1383in in spain"
x=re.findall("[^0-7]",txt)
print(x)