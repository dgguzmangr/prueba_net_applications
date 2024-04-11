import os

path = r'\C:\Users\DAVID GUZMAN\OneDrive\Escritorio\David\'

def mappFiles(path):
    # primero verifico que la ruta es válida
    if not os.path.isdir(path):
        return "La  ruta no existe"
    # crear una lista para guardar los nombres de los archivos
    files = os.listdir(path)
    q_files = len(files)
    
    return q_files, f"archivos en {path}"


x = mappFiles(path)
print(x)