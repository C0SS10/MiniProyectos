import lyricsgenius

genius = lyricsgenius.Genius("1Ijg3OiScqAB8RS3pC3bdajuYLDo9g3ss5QCYSqHLilNySf4CGMgkHxh5LBfNTU1")

def obtener_barras(temas, artista, album):
    nombre_tema = temas
    tema = genius.search_song(nombre_tema,artista)

    if not tema:
        return print("No se pudo encontrar la canción")

    barrotes = tema.lyrics

    with open('API_Genius/canciones/{}/{}_{}.txt'.format('_'.join(artista.split(' ')),artista,'-'.join(''.join(nombre_tema.split('\'')).split(' '))),'a') as f:
        f.writelines(barrotes.split('\\n'))

def escribir():
    n_tema = input("Escriba el nombre de la canción: ")
    n_artista = input("Escriba el nombre del artista: ")
    n_album = input("Escriba el nombre del album: ")

    obtener_barras(n_tema,n_artista,n_album)