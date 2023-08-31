# import tkinter as tk
# from bs4 import BeautifulSoup
# import requests
# from PIL import Image, ImageTk

# def scrape_and_display():
#     URL_BASE = 'https://cuevana3.nu/genero/accion/'
#     pedido_obtenido = requests.get(URL_BASE)
#     html_obtenido = pedido_obtenido.text
#     soup = BeautifulSoup(html_obtenido, "html.parser")

#     pelicula_titulos = soup.find_all('div', class_='TPostMv')

#     pelicula_info_list = []

#     for pelicula_titulo in pelicula_titulos:
#         imagen_div = pelicula_titulo.find('div', class_='Image')

#         if imagen_div:
#             imagen_url = imagen_div.find('img')['data-src']
#             titulo = imagen_div.find('img')['alt']
#             info_div = pelicula_titulo.find('div', class_='TPMvCn')
            
#             if info_div:
#                 year_span = info_div.find('span', class_='Date')
#                 year = year_span.text.strip() if year_span else "No disponible"
                
#                 time_span = info_div.find('span', class_='Time')
#                 duration = time_span.text.strip() if time_span else "No disponible"

#             pelicula_info = f"Titulo: {titulo}\nAño: {year}\nDuración: {duration}\n"
#             pelicula_info_list.append((pelicula_info, imagen_url))

#     for pelicula_info, imagen_url in pelicula_info_list:
#         result_label.config(text=pelicula_info)
            
#         imagen_pil = Image.open(requests.get(imagen_url, stream=True).raw)
#         imagen_pil = imagen_pil.resize((200, 300))  # Resize the image to fit the label
#         imagen_tk = ImageTk.PhotoImage(imagen_pil)
            
#         image_label.config(image=imagen_tk)
#         image_label.image = imagen_tk

#         root.update()  # Update the UI to show each movie

# root = tk.Tk()
# root.title("Scraping App")

# scrape_button = tk.Button(root, text="Scrapear Películas", command=scrape_and_display)
# scrape_button.pack()

# result_label = tk.Label(root, text="", justify="left")
# result_label.pack()

# image_label = tk.Label(root)
# image_label.pack()

# root.mainloop()


import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageTk

def on_scroll(*args):
    canvas.yview(*args)
    result_frame.yview(*args)

def scrape_and_display():
    URL_BASE = 'https://cuevana3.nu/genero/accion/'
    pedido_obtenido = requests.get(URL_BASE)
    html_obtenido = pedido_obtenido.text
    soup = BeautifulSoup(html_obtenido, "html.parser")

    pelicula_titulos = soup.find_all('div', class_='TPostMv')

    pelicula_info_list = []

    for pelicula_titulo in pelicula_titulos:
        imagen_div = pelicula_titulo.find('div', class_='Image')

        if imagen_div:
            imagen_url = imagen_div.find('img')['data-src']
            titulo = imagen_div.find('img')['alt']
            info_div = pelicula_titulo.find('div', class_='TPMvCn')
            
            if info_div:
                year_span = info_div.find('span', class_='Date')
                year = year_span.text.strip() if year_span else "No disponible"
                
                time_span = info_div.find('span', class_='Time')
                duration = time_span.text.strip() if time_span else "No disponible"

            pelicula_info = f"Titulo: {titulo}\nAño: {year}\nDuración: {duration}\n"
            pelicula_info_list.append((pelicula_info, imagen_url))

    for pelicula_info, imagen_url in pelicula_info_list:
        imagen_pil = Image.open(requests.get(imagen_url, stream=True).raw)
        imagen_pil = imagen_pil.resize((300, 200))  # Resize the image to fit the label
        imagen_tk = ImageTk.PhotoImage(imagen_pil)
            
        pelicula_label = tk.Label(result_frame, text=pelicula_info, image=imagen_tk, compound='top', justify="left")
        pelicula_label.image = imagen_tk
        pelicula_label.pack()

    root.update()  # Update the UI after displaying all movies

root = tk.Tk()
root.title("DEPRIVAGEITOR 2.0")
root.geometry("400x1080")  # Tamaño de la ventana

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

result_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=result_frame, anchor="nw")

scrape_and_display()

root.mainloop()


