import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if len(rostos) > 0:
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    antonio1 = reconhece_face("./img/antonio1.jpeg")
    if(antonio1[0]):
        rostos_conhecidos.append(antonio1[1][0])
        nomes_dos_rostos.append("Antonio")

    marcolan1 = reconhece_face("./img/marcolan1.jpeg")
    if(marcolan1[0]):
        rostos_conhecidos.append(marcolan1[1][0])
        nomes_dos_rostos.append("Marchongus")
        
    traba1 = reconhece_face("./img/traba1.jpeg")
    if(traba1[0]):
        rostos_conhecidos.append(traba1[1][0])
        nomes_dos_rostos.append("Traba")
    
    return rostos_conhecidos, nomes_dos_rostos