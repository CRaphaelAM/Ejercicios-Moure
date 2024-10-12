"""
*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */
"""


import requests
from PIL import Image
from io import BytesIO

def get_image(url:str):
    response = requests.get(url)
    print(response.status_code)
    
    return response

def calcular_aspect_ratio(imagen:Image)->float:
    width, height = imagen.size()
    return width/height

def main()->None:
    url = "https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png"
    response = get_image(url)

    imagen = Image.open(BytesIO(response.content))

    ratio = calcular_aspect_ratio(imagen)

    print(f"El aspect ratio de la imagen es: {ratio}")



if __name__ == "__main__":
    main()