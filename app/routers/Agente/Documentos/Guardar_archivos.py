import base64
from datetime import datetime
import random
import string

async def guardar_archivos(archivo, tipo):
    
    date = str( datetime.today().strftime('%Y-%m-%d'))
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(50))
    ruta = date + random_string
        
    if tipo == "pdf":    
        archivo_decodificado = base64.b64decode(archivo)
        pdfFile = open(f"app/Agentes_files/{ruta}.pdf", 'wb')
        pdfFile.write(archivo_decodificado)
        pdfFile.close()     
        
        return ruta+".pdf"
    
    elif tipo == "img":   
        archivo_decodificado = base64.b64decode(archivo)
        pdfFile = open(f"app/Agentes_files/{ruta}.jpg", 'wb')
        pdfFile.write(archivo_decodificado)
        pdfFile.close()     
        
        return ruta+".jpg"