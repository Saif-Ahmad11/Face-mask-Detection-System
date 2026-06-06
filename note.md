face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

Loads a pred-trained face detector.

OpenCV contains buit-in Haar Cascade XML files
Detects.
-> eyes
->nose
->facial patterns

cap = cv2.VideoCapture(0)
--> Starts webcam capture

success, frame = cap.read()
--> Reads image from webcam

gray = cv2.cvColor(frame, cv2.COLOR_BGR2GRAY)
--> Face detection is faster on grayscale images.

face  = face_classifier.detectMultiScale(gray, 1.1, 5)
1.1 --> Scale facter. Controls image reduction during detection
5 --> Minimum neighbors.

for (x,y,w,h) in faces:
--> Processes each detected face separately.
    face = frame[y:y+h, x:x+w]
--> Cuts only the face area.