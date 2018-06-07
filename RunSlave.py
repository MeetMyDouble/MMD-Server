import sys
from opencv import find_faces_in_picture_cnn
import os
import face_recognition
import time



def main():
    if len(sys.argv ) < 2:
        print("Usage : python3 RunSlave.py <slaveport>")
        return

    if not os.path.exists("tmp/" + sys.argv[1]):
        os.mkdir("tmp/" + sys.argv[1])

    path = "tmp/" + sys.argv[1]

    while (True):
        files = os.listdir(path)
        if len(files) > 0:
            print("fichier trouvé")
            image = face_recognition.load_image_file(path + '/' + files[0])
            os.remove(path + '/' + files[0])
            find_faces_in_picture_cnn.find_faces(image, files[0])

        time.sleep(1)



    #app.run('127.0.0.1', sys.argv[1])



if __name__ == '__main__':
    main()