import re
orig = (open('p13input','r')).read()
fixed = re.sub('(\n)',' ',orig)
(open('p13inputFixed','w')).write(fixed)