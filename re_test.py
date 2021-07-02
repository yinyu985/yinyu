import re

str = "abc123def"
text = re.search(r'[0-9]+',str,)
print(text)
