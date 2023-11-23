""" 
2-4 f: fgff
4-6 z: zzzsg
1-6 h: hhhhhh
Cada línea indica, separado por :, la política de la clave y la clave misma 
"""
COUNT_BAD = 0

def validate_password(txt):
  global COUNT_BAD
  for line in txt:
    policy, password = line.split(":")
    limits, letter = policy.split(" ")
    limit_min, limit_max = limits.split("-")
    limit_min = int(limit_min)
    limit_max = int(limit_max)
    if is_valid(limit_min, limit_max, letter, password):
      pass
    else:
      COUNT_BAD += 1
      if (COUNT_BAD == 42 or COUNT_BAD == 13):
        print (f"Password {COUNT_BAD}: {password} is invalid ❗")


def is_valid(limit_min, limit_max, letter, password):
  if limit_min <= password.count(letter) <= limit_max:
    return True
  return False

if __name__ == "__main__":
  with open("message_03.txt", "r") as txt:
    txt = txt.readlines()
    validate_password(txt)