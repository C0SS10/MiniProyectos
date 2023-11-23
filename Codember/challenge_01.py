# Reto 1: Crear un patrón para identificar palabras y sus repeticiones
def count_words(text):
    wordsDict = {}
    text = text.lower()
    for word in text.split(" "):
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    
    format_string(wordsDict)

# Formatear el diccionario para que tenga un formato 'perro1sol3gato2'
def format_string(wordsDict):
    formattedString = ""
    for key in wordsDict:
        formattedString += (key + str(wordsDict[key]))

    print(formattedString)

# Crear un main
if __name__ == "__main__":
    txt = open("message_01.txt", "r")
    count_words(txt.read())