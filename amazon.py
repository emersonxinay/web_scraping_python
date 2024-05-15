import requests
from bs4 import BeautifulSoup


def obtener_precios_mas_bajos(query):
    url = f"https://www.amazon.com/s?k={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    productos = []
    resultados = soup.find_all("div", class_="s-result-item")

    for resultado in resultados:
        titulo = resultado.find("span", class_="a-text-normal").text.strip()
        precio = resultado.find("span", class_="a-offscreen")
        if precio:
            precio = precio.text.strip()
        else:
            precio = "Precio no disponible"
        productos.append({"Titulo": titulo, "Precio": precio})

    return productos


if __name__ == "__main__":
    query = input("Ingrese el producto que desea buscar en Amazon: ")
    precios = obtener_precios_mas_bajos(query)

    for producto in precios:
        print(producto["Titulo"])
        print(producto["Precio"])
        print("-" * 50)
