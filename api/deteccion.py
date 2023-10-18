import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

# Carga el modelo preentrenado
model = keras.models.load_model('C:/Users/jonat/Escritorio/pulmonia.h5')

def deteccion_neumonia(imagen):
    if isinstance(imagen, InMemoryUploadedFile):
        # Lee el contenido de la imagen en un búfer de bytes
        buffer = BytesIO(imagen.read())
        
        # Convierte el búfer de bytes en una matriz NumPy
        np_image = np.frombuffer(buffer.getvalue(), dtype=np.uint8)
        
        # Decodifica la matriz NumPy en una imagen
        imagen = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        # Redimensiona la imagen según los requisitos de tu modelo (por ejemplo, 224x224)
        imagen = cv2.resize(imagen, (224, 224))
        
        # Realiza cualquier otro preprocesamiento necesario, como normalización
        imagen = imagen / 255.0  # Normalización (si es necesario)

        # Realiza la predicción utilizando el modelo
        resultado = model.predict(np.expand_dims(imagen, axis=0))[0]
        porcentaje_acierto1 = np.max(resultado[0]) * 100
        porcentaje_acierto2 = np.max(resultado[1]) * 100
        
        # Determina si la imagen tiene neumonía o no
        if resultado[0] > resultado[1]:
            nueva = False
              #Sin neumonía
        else:
            nueva = True  #Con neumonía
        return{
            'resultado': nueva,
            'confiabilidad_no': round(porcentaje_acierto1,2),
            'confiabilidad_si': round(porcentaje_acierto2,2)
        }    
    else:
        return False  # Devuelve un valor predeterminado si la imagen no es válida