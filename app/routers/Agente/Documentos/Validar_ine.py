import base64
import random
import string
from datetime import datetime
import pytesseract
from PIL import Image
import os

async def validar_ine(archivo):
   validate = False
   try:
      date = str( datetime.today().strftime('%Y-%m-%d'))
      letters = string.ascii_lowercase
      random_string = ''.join(random.choice(letters) for i in range(50))
      ruta = date + random_string
      
      archivo_decodificado = base64.b64decode(archivo)
      imgFile = open(f"app/Agentes_files/{ruta}.jpg", 'wb')
      imgFile.write(archivo_decodificado)
      imgFile.close()     
      ruta = ruta+".jpg"
         
      pytesseract.pytesseract.tesseract_cmd = r'C:\Users\eescobar\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
      
      img = Image.open(f"app/Agentes_files/{ruta}")
      text = pytesseract.image_to_string(img)
      
      valores_buscar = ['INSTITUTO NACIONAL ELECTORAL',
                        'CREDENCIAL PARA VOTAR'
                        ]
      validate = True
      for valor in valores_buscar: 
         if(text.find(valor) == -1):
            validate = False 
            
      imgFile.close();           
      file_path = (f"app/Agentes_files/{ruta}")
      os.remove(file_path)
         
      return validate
      
   except:   
      return validate
   