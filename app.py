import re
texte = "Contactez-moi à email@example.com ou support@domain.org"
regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"  # Complète ici
print(re.findall(regex, texte))