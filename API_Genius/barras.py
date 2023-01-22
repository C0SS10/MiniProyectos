import lyricsgenius
import os

genius = lyricsgenius.Genius("API Key")

def obtener_barras(temas, artista):
    nombre_tema = temas
    tema = genius.search_song(nombre_tema,artista)

    if not tema:
        return print("No se pudo encontrar la canción")

    barrotes = tema.lyrics

    with open('API_Genius/canciones/{}/{}-{}.txt'.format(artista,artista,' '.join(''.join(nombre_tema.split('\'')).split(' '))),'a') as f:
        f.writelines(barrotes.split('\\n'))

def escribir():
    caracteres = '\/:*?|"<>'
    x = input("Escriba el nombre de la canción: ")
    y = input("Escriba el nombre del artista: ")
    n_artista = y.replace(' ','_')
    n_tema = x.replace(caracteres,' ')
    if os.path.exists(f'API_Genius/canciones/{n_artista}'):
        obtener_barras(n_tema,n_artista)
    else:
        os.makedirs(f'API_Genius/canciones/{n_artista}')
        obtener_barras(n_tema,n_artista)