import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    smiles=smile_cascade.detectMultiScale(gray,1.7,22)
    cv2.putText(img,f"You're on Camera...Smile!", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)
   
    for (sx, sy, sw, sh) in smiles:
            
            cv2.rectangle(img, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
            cv2.putText(img, "Smiling :)", (sx, sy), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow('Smile Detector', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
