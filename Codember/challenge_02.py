"""
"#" Incrementa el valor numérico en 1.
"@" Decrementa el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual.
"""
INITIAL_NUMBER = 0

def compile(stack):
  global INITIAL_NUMBER
  tokens = list(stack)
  output = ""
  for token in tokens:
    if token == "#":
      INITIAL_NUMBER += 1
      print(f"Increase: {INITIAL_NUMBER}")
    elif token == "@":
      INITIAL_NUMBER -= 1
      print(f"Decrease {INITIAL_NUMBER}")
    elif token == "*":
      INITIAL_NUMBER *= INITIAL_NUMBER
      print(f"Multiply: {INITIAL_NUMBER}")
    elif token == "&":
      output += str(INITIAL_NUMBER)
      print(f"Printing: {INITIAL_NUMBER}")
  
  return output


if __name__ == "__main__":
  with open("message_02.txt", "r") as txt:
    output = compile(txt.read())
  print(output)