from PIL import Image
import face_recognition
import numpy
import os

def find_faces(image, pictureName):
    # Load the jpg file into a numpy array
    #image = face_recognition.load_image_file("queue/" + temporary)

    #os.remove("queue/" + temporary)


    # Find all the faces in the image using a pre-trained convolutional neural network.
    # This method is more accurate than the default HOG model, but it's slower
    # unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
    # this will use GPU acceleration and perform well.
    # See also: find_faces_in_picture.py

    print("Scanning picture....")
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

    rotation = 0

    if len(face_locations) == 0:
        print("No face found, rotating picture")
        print("Scanning picture....")
        fullpic = Image.fromarray(image)
        fullpic = fullpic.rotate(90)
        rotation += 90
        pix = numpy.array(fullpic)
        face_locations = face_recognition.face_locations(pix, number_of_times_to_upsample=0, model="cnn")

    if len(face_locations) == 0:
        print("No face found, rotating picture")
        print("Scanning picture....")
        fullpic = Image.fromarray(image)
        fullpic = fullpic.rotate(90)
        rotation += 90
        pix = numpy.array(fullpic)
        face_locations = face_recognition.face_locations(pix, number_of_times_to_upsample=0, model="cnn")

    if len(face_locations) == 0:
        print("No face found, rotating picture")
        print("Scanning picture....")
        fullpic = Image.fromarray(image)
        fullpic = fullpic.rotate(90)
        rotation += 90
        pix = numpy.array(fullpic)
        face_locations = face_recognition.face_locations(pix, number_of_times_to_upsample=0, model="cnn")



    print("Found {} face(s) in this photograph.".format(len(face_locations)))

    if len(face_locations) > 1:
        print("found more than one face. Cannot save it")
        return

    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        print("Rotation {}".format(rotation))
        pil_image = pil_image.rotate(rotation)

        splittedPictureName = str.split(pictureName, '.')

        splittedPictureName.remove(splittedPictureName[len(splittedPictureName) - 1])

        username = str.join('.', splittedPictureName)

        print("Le nom d'utilisateur : ")
        print(username)

        if not os.path.exists("pictures/" + username):
            os.mkdir("pictures/" + username)


        files = os.listdir("pictures/" + username)


        pil_image.save("pictures/" + username + '/' + str(len(files) + 1) +  pictureName)


