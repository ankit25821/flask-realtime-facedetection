import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def detect_face(image):

    # Convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    image = cv2.imencode('.jpeg', image, [cv2.IMWRITE_JPEG_QUALITY, 40])[1]

    return image
