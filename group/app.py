import re
text = "Mon numéro est 123-456-7890"
regex = r"(\d{3})-(\d{3})-(\d{4})"
match = re.search(regex, text)
print(match.group(1))
print(match.group(2))
print(match.group(3))