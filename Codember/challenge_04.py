""" 
Cada archivo tiene un nombre con dos partes, separadas por un guion (-). 
La primera parte es una cadena alfanumérica y la segunda es unchecksum, 
que es una cadena formada por los caracteres que sólo aparecen una vez en la primera parte 
y en el orden en que aparecen.
"""
COUNT_REAL = 0

def check_file(txt):
  global COUNT_REAL
  for i, line in enumerate(txt):
    name, checksum = line.strip().split("-")
    if is_valid(name, checksum):
      if i == 34:
        print(f"{i + 1}. File {name} is valid ✅")
    else:
      pass


def is_valid(name, checksum):
  name = name.replace("-", "")
  unique_characters = []
    
  for letter in name:
    if name.count(letter) == 1:
      unique_characters.append(letter)
    
  calculated_checksum = ''.join(unique_characters)
    
  return calculated_checksum == checksum


if __name__ == "__main__":
  with open("message_04.txt", "r") as txt:
    txt = txt.readlines()
    check_file(txt)
