#Challenge5
'''
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
'''
import urllib.request
from PIL import Image

def challenge5():
    urllib.request.urlretrieve(
  'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png',
   "gfg.png")
  
    img = Image.open("gfg.png")

    width,height = img.size
  
    # display width and height
    print(f'La Altura de la imagen es: ', height)
    print(f'El ancho de la imagen es :', width)
    print(f'El ratio es: ', (width/height))

    img.show()

challenge5()
