import base64
import PyPDF2
import random
import string
import os
from datetime import datetime

async def validar_constancia_fiscal(archivo):
    validate = False
    try:
        date = str( datetime.today().strftime('%Y-%m-%d'))
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(50))
        ruta = date + random_string
            
        archivo_decodificado = base64.b64decode(archivo)
        pdfFile = open(f"app/Agentes_files/{ruta}.pdf", 'wb')
        pdfFile.write(archivo_decodificado)
        pdfFile.close()     
        ruta = ruta+".pdf"
            
        v_pdfFile = open(f"app/Agentes_files/{ruta}", 'rb')
        v_pdf_reader = PyPDF2.PdfFileReader(v_pdfFile)    
        
        v_texto= ''
        for page in range(v_pdf_reader.getNumPages()):
            v_pdf_objeto = v_pdf_reader.getPage(page)
            v_texto += v_pdf_objeto.extract_text()
            
        valores_buscar = ['CÉDULA DE IDENTIFICACIÓN FISCAL',
                        'Registro Federal de Contribuyentes',
                        'Nombre, denominación o razón',
                        'VALIDA TU INFORMACIÓN',
                        'CONSTANCIA DE SITUACIÓN FISCAL',
                        'Lugar y Fecha de Emisión',
                        'RFC',
                        'CURP',
                        'Nombre(s)',
                        'PrimerApellido',
                        'Segundo Apellido',
                        'Fechainiciodeoperaciones',
                        'Estatusenelpadrón',
                        'Fechadeúltimocambiodeestado',
                        'NombreComercial',
                        'CódigoPostal',
                        'TipodeVialidad',
                        'NombredeVialidad',
                        'NúmeroExterior',
                        'NúmeroInterior',
                        'NombredelaColonia',
                        'Nombre delMunicipio oDemarcación Territorial',
                        'NombredelaLocalidad',
                        'NombredelaEntidadFederativa',
                        'EntreCalle',
                        'YCalle',
                        'Regímenes',
                        'Régimen',
                        'Fecha Inicio',
                        'Fecha Fin'
                        ]
        
        validate = True
        for valor in valores_buscar: 
            if(v_texto.find(valor) == -1):
                validate = False 
    
        pdfFile.close();   
        v_pdfFile.close(); 
            
        file_path = (f"app/Agentes_files/{ruta}")
        os.remove(file_path)
    
        return validate 
    except:  
        return validate  
      