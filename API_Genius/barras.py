import lyricsgenius
import os

genius = lyricsgenius.Genius("1Ijg3OiScqAB8RS3pC3bdajuYLDo9g3ss5QCYSqHLilNySf4CGMgkHxh5LBfNTU1")

def obtener_barras(temas, artista, album):
    nombre_tema = temas
    tema = genius.search_song(nombre_tema,artista)

    if not tema:
        return print("No se pudo encontrar la canción")

    barrotes = tema.lyrics

    with open('API_Genius/canciones/{}/{}-{}.txt'.format(artista,artista,' '.join(''.join(nombre_tema.split('\'')).split(' '))),'a') as f:
        f.writelines(barrotes.split('\\n'))

def escribir():
    n_tema = input("Escriba el nombre de la canción: ")
    n_artista = input("Escriba el nombre del artista: ")
    n_album = input("Escriba el nombre del album: ")
    x = n_artista.replace(' ','_')
    y = n_tema.replace(':',' ')
    if os.path.exists(f'API_Genius/canciones/{x}'):
        obtener_barras(y,x,n_album)
    else:
        os.makedirs(f'API_Genius/canciones/{x}')
        obtener_barras(y,x,n_album)