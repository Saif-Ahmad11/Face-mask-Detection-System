import cv2
import numpy as np
from tensorflow.keras.models import load_model
# load model
model = load_model("face_mask_model.keras", compile=False)
# Face detector
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face  = face_classifier.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in face:
        face = frame[y:y+h, x:x+w]
        face = cv2.resize(face, (100,100))
        face = face/255.0
        face = np.reshape(face, (1,100,100,3))
        prediction = model.predict(face, verbose = 0)
        label = np.argmax(prediction)
        if label == 0:
            text = "Mask"
            color = (0,255,0)
        else:
            text = "No Mask"

            color = (0,0,255)    
        cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
        cv2.putText(frame, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    cv2.imshow("Face Mask Detection", frame)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()