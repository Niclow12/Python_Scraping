from bs4 import BeautifulSoup
import requests

URL_BASE = 'https://cuevana3.nu/genero/accion/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, "html.parser")

pelicula_titulos = soup.find_all('div', class_='TPostMv')

for pelicula_titulo in pelicula_titulos:
    imagen_div = pelicula_titulo.find('div', class_='Image')

    if imagen_div:
        imagen = imagen_div.find('img')['data-src']
        titulo = imagen_div.find('img')['alt']
        info_div = pelicula_titulo.find('div', class_='TPMvCn')
        print("Titulo:", titulo)
        
        if info_div:
            year_span = info_div.find('span', class_='Date')
            if year_span:
                year = year_span.text.strip()
                print("Año:", year)
            
            time_span = info_div.find('span', class_='Time')
            if time_span:
                duration = time_span.text.strip()
                print("Duración:", duration)
            
            

        print("Imagen:", imagen)
        print("=" * 40)
    else:
        print("Imagen not found")
