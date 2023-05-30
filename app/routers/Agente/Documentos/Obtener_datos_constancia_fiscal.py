import fitz
import base64
import PyPDF2
import random
import string
import os
from datetime import datetime

async def obtener_datos_constancia_fiscal(archivo):
    
    date = str( datetime.today().strftime('%Y-%m-%d'))
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(50))
    ruta = date + random_string
        
    archivo_decodificado = base64.b64decode(archivo)
    pdfFile = open(f"app/Agentes_files/{ruta}.pdf", 'wb')
    pdfFile.write(archivo_decodificado)
    pdfFile.close()     
    ruta = ruta+".pdf"
        
    path = f"app/Agentes_files/{ruta}"
    doc = fitz.open(path)
    
    text = ''
    for page in doc:
        text += page.get_text()
                
    pdfFile.close();   
    doc.close();   
        
    file_path = (f"app/Agentes_files/{ruta}")
    os.remove(file_path)       
    
    nombres = await crear_dict(text, "\nNombre (s):\n", "\nPrimer Apellido:\n", "nombres")
    rfc = await crear_dict(text, "\nRFC:\n", "\nCURP:\n", "rfc")
    curp = await crear_dict(text, "\nCURP:\n", "\nNombre (s):\n", "curp")
    apellido_pat = await crear_dict(text, "\nPrimer Apellido:\n", "\nSegundo Apellido:\n", "apellido_pat")
    apellido_mat = await crear_dict(text, "\nSegundo Apellido:\n", "\nFecha inicio de operaciones:\n", "apellido_mat")
    codigo_postal = await crear_dict(text, "\nCódigo Postal:", "\nTipo de Vialidad: CALLE\n", "codigo_postal")
    calle = await crear_dict(text, "\nNombre de Vialidad:", "\nNúmero Exterior:", "calle")
    no_ext = await crear_dict(text, "\nNúmero Exterior:", "\nNúmero Interior:", "no_ext")
    no_int = await crear_dict(text, "\nNúmero Interior:", "\nNombre de la Colonia:", "no_int")
    colonia = await crear_dict(text, "\nNombre de la Colonia:", "\nNombre de la Localidad:", "colonia")
    delegacion_municipio = await crear_dict(text, "\nNombre\ndel\nMunicipio\no\nDemarcación\nTerritorial:\n", "\nNombre de la Entidad Federativa:", "delegacion_municipio")
    estado = await crear_dict(text, "\nNombre de la Entidad Federativa:", "\nEntre Calle:", "estado")           
    
    datos_usuario = {
      "nombres": nombres.lstrip().replace('\n', ' '),
      "rfc": rfc.lstrip().replace('\n', ' '),
      "curp": curp.lstrip().replace('\n', ' '),
      "apellido_pat": apellido_pat.lstrip().replace('\n', ' '),
      "apellido_mat": apellido_mat.lstrip().replace('\n', ' '),
      "codigo_postal": codigo_postal.lstrip().replace('\n', ' '),
      "calle": calle.lstrip().replace('\n', ' '),
      "no_ext": no_ext.lstrip().replace('\n', ' '),
      "no_int": no_int.lstrip().replace('\n', ' '),
      "colonia": colonia.lstrip().replace('\n', ' '),
      "delegacion_municipio": delegacion_municipio.lstrip().replace('\n', ' '),
      "estado": estado.lstrip().replace('\n', ' ')
    }
     
    return datos_usuario 

async def crear_dict(cadena, str_inicio, str_fin, dato):
    inicio = str_inicio
    fin = str_fin

    indice_inicio = cadena.find(inicio) + len(inicio)
    indice_final = cadena.find(fin)
    if dato == 'nombres':
        nombres = cadena[indice_inicio:indice_final]
        return nombres
    elif dato == 'rfc':
        rfc = cadena[indice_inicio:indice_final]
        return rfc
    elif dato == 'curp':
        curp = cadena[indice_inicio:indice_final]
        return curp  
    elif dato == 'apellido_pat':
        apellido_pat = cadena[indice_inicio:indice_final]
        return apellido_pat
    elif dato == 'apellido_mat':
        apellido_mat = cadena[indice_inicio:indice_final]
        return apellido_mat
    elif dato == 'codigo_postal':
        codigo_postal = cadena[indice_inicio:indice_final]
        return codigo_postal
    elif dato == 'calle':
        calle = cadena[indice_inicio:indice_final]
        return calle
    elif dato == 'no_ext':
        no_ext = cadena[indice_inicio:indice_final]
        return no_ext
    elif dato == 'no_int':
        no_int = cadena[indice_inicio:indice_final]
        return no_int
    elif dato == 'colonia':
        colonia = cadena[indice_inicio:indice_final]
        return colonia
    elif dato == 'delegacion_municipio':
        delegacion_municipio = cadena[indice_inicio:indice_final]
        return delegacion_municipio
    elif dato == 'estado':
        estado = cadena[indice_inicio:indice_final]
        return estado
    
        
     