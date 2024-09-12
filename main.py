import os
import shutil
from pathlib import Path

# Definir la carpeta de descargas que quieres organizar
path_downloads = Path.home() / "Downloads" # Descargas si es en español.

print(path_downloads)

# Crear carpetas para diferentes tipos de archivos
categorias = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Iconos": [".ico"],
    "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".csv", ".doc", ".xls"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archivos comprimidos": [".zip", ".rar", ".7z"],
    "querys": [".sql"],
    "backups": [".bak", ".backup"],
    "scripts": [".js", ".py", "ipynb", ".css", ".c", ".php", ".cpp", ".tsx", ".ts"],
    "ejecutables": [".exe", ".msi", ".iso"],
    "archivos de texto": [".txt"],
    "Power Bi": [".pbix"],
    "Json": [".json"],
    "Paginas": [".html", ".xml", ".webp"],
    "logs": [".log"],
    "Arhivos de sistema": [".dll", ".ini"]
}

# Crear carpetas si no existen
for categoria in categorias:
    (path_downloads / categoria).mkdir(exist_ok=True)

# Mover archivos a sus respectivas carpetas
for archivo in path_downloads.iterdir():
    if archivo.is_file():
        extension = archivo.suffix.lower()
        for categoria, extensiones in categorias.items():
            if extension in extensiones:
                shutil.move(str(archivo), str(path_downloads / categoria / archivo.name))
                break

print("Carpeta de descargas organizada.")