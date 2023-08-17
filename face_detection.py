import cv2

face_classifer = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_cropped(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifer.detectMultiScale(gray,1.3,5)
    #1.3 scaling Factor 5 Minimum Neighbour

    for (x,y,w,h) in faces:
        face_cropped = img[y:y+h,x:x+w]
        return face_cropped

try:
    cap = cv2.VideoCapture(0)
    img_id =0
    id = 1
    while True:
        ret,my_frame = cap.read()
        if face_cropped(my_frame)is not None:
            img_id  += 1
            face = cv2.resize(face_cropped(my_frame),(450,450))
            face = cv2.cvtColor(face , cv2.COLOR_BGR2GRAY)
            file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
            cv2.imwrite(file_name_path,face)
            cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
            cv2.imshow("Cropped Face",face)

        if cv2.waitKey(1) == 13 or int(img_id) == 100:
            break

    cap.release()
    cv2.destroyAllWindows()

    print("completed")
except Exception as es:
    print(str(es))

