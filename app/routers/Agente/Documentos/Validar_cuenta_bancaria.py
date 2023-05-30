import base64
import random
import string
from datetime import datetime
import pytesseract
from PIL import Image
import os

async def validar_cuenta_bancaria(archivo):
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
      
      bancos = ['BANORTE','Libretén Basico Cuenta Digital']
      
      banco = ''
      for valor in bancos: 
         if text.find(valor) == 17:
            banco = "BBVA"
         elif text.find(valor) == 26:
            banco = "BANORTE"
            
      validate = True
      
      if banco == "BBVA":
            valores_buscar = ['SUCURSAL',
                              'DIRECCION',
                              'MONEDA NACIONA',
                              'Manejo de Cuenta',
                              'Comisiones'
                              ]
            
            for valor in valores_buscar: 
               if(text.find(valor) == -1):
                  validate = False 
                  
            imgFile.close();           
            file_path = (f"app/Agentes_files/{ruta}")
            os.remove(file_path)
               
            return validate

      elif banco == "BANORTE":
            valores_buscar = ['Periodo Del',
                           'Moneda',
                           'NO. DE CLIENTE',
                           'RFC',
                           'DATOS DE SUCURSAL',
                           'PLAZA',
                           'DIRECCION',
                           'TELEFONO',
                           'Producto',
                           'No. de Cuenta',
                           'CLABE',
                           'Saldo anterior'
                           ]
            for valor in valores_buscar: 
               if(text.find(valor) == -1):
                  validate = False 
                  
            imgFile.close();           
            file_path = (f"app/Agentes_files/{ruta}")
            os.remove(file_path)
               
            return validate
         
      else:
         return validate 
   except:
      return validate
         
  
      
   
            
   
    