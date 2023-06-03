from deepface import DeepFace
import cv2


webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        try:
            face_analysis = DeepFace.analyze(frame, actions=['emotion'])
            region = face_analysis[0]['region']
            pt1 = region['x'], region['y']
            pt2 = region['x'] + region['w'], region['y'] + region['h']

            cv2.rectangle(frame, pt1=pt1, pt2=pt2, color=(241, 242, 64), thickness=1)
            
            emotion = face_analysis[0]['dominant_emotion']
            emotion_per = str(round(face_analysis[0]['emotion'][emotion], 1) )
            cv2.putText(frame, 'Emotion: ' + emotion + ' ' + emotion_per + '%', (pt1[0]+10, pt1[1]+region['h']+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (241, 242, 64), 1, cv2.LINE_AA)

            cv2.imshow("test", frame)

        except:
            pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

