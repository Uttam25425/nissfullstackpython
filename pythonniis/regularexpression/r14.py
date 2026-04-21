import re
txt="The ra16283in in sp4a9i6n"
x=re.findall("[0-9][a-z]",txt)
print(x)