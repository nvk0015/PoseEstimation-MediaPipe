import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture("Videos/2.mp4")
pTime = 0
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.resize(img,(720,480))
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            #print(id, lm)
            cx,cy = int(lm.x*w),int(lm.y*h)
            cv2.circle(img,(cx,cy),6,(0,255,0),cv2.FILLED)

    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_ITALIC,2,(255,0,0),2)
    cv2.imshow("MediaPipe Estimator",img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()