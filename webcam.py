import numpy as np
import face_recognition as fr
import cv2
import serial
import time
from engine import get_rostos

rostos_conhecidos, nome_dos_rostos = get_rostos()
arduino = serial.Serial('COM7', 9600)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    
    rgb_frame = frame[:,:,::-1]
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    localizacao_dos_rostos = fr.face_locations(rgb_frame)
    if len(localizacao_dos_rostos) == 0:
        continue
    rostos_desconhecidos = fr.face_encodings(rgb_frame, localizacao_dos_rostos)
    '''
    rostos_desconhecidos = []
    for localizacao_rosto in localizacao_dos_rostos:
        top, right, bottom, left = localizacao_rosto
        rosto_desconhecido = rgb_frame[top:bottom, left:right]
        encoding_rosto_desconhecido = fr.face_encodings(rosto_desconhecido)
        if len(encoding_rosto_desconhecido) > 0:
            rostos_desconhecidos.append(encoding_rosto_desconhecido[0])'''
    
    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rostos_desconhecidos):
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
        print(resultados)
        
        face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecido)
        
        best_id = np.argmin(face_distances)
        if resultados[best_id]:
            name = nome_dos_rostos[best_id]
        else:
            name = "Desconhecido"
            
        if resultados[best_id]:
            name = nome_dos_rostos[best_id]
            arduino.write(b'1')  
            time.sleep(0.15)
            arduino.write(b'0')
            time.sleep(0.2)
            arduino.write(b'1')  
            time.sleep(0.15)
            arduino.write(b'0')
            time.sleep(2)
            
            
        else:
            name = "Desconhecido"
            arduino.write(b'0')  

        
        cv2.rectangle(frame, (left,top), (right,bottom), (0,255,0), 2)
        
        cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0,255,0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.putText(frame, name, (left+6,bottom-6), font, 1.0, (255,255,255), 1)
    
    cv2.imshow('Webcam_facerecognition', frame)
        
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
arduino.close()