import cv2 ,sys , numpy , os 

haar_file = "C:/Users/Anukriti/Desktop/all my files (anukriti)/python/projects/open cv/l-8/haarcascade_frontalface_default.xml"
datasets="C:/Users/Anukriti/Desktop/all my files (anukriti)/python/projects/open cv/l-8/dataset"

sub_data="Anukriti"

path = os.path.join(datasets,sub_data)
print(path)
a=os.path.isdir(path) 
print(a)

if not os.path.isdir(path):
    os.mkdir(path) #new foler


(width,height)=(130,100)

face_cascade=cv2.CascadeClassifier(haar_file)
   
#0 is for web cam
#cam attached use 1

webcam=cv2.VideoCapture(0)

count=1

while count < 30:
    (ret, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('% s/% s.png' % (path, count), face_resize)
    count += 1
     
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(0)
    if key == 27:
        break