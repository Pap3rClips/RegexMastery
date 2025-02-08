import re

texte = "J'ai 3 pommes et 20 oranges, soit 23 fruits."
regex = r"[\d+]"  # Complète ici
print(re.findall(regex, texte))