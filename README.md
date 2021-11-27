# PoseEstimation-MediaPipe

# Videos
The videos folder consists 10 videos downloaded from an open source website - https://www.pexels.com/ 
The idea is to detect the keypoints on these videos

# PoseEstimationBasic.py 
It is a python development file through which we use the OpenCV, Google's Mediapipe libraries to read, detect lanmarks, draw connections, and then display back the video on a window. One drawback of Mediapipe Pose estimation is its disability to higher accuracy for detections on multi-person videos or images.
The technical details of the model architectures, accuracies, and helper functions to detect landmarks, draw connections are in detail on their website -https://google.github.io/mediapipe/solutions/pose.html

# PoseModule.py
This module is still under development. The intention to develop this module is to have better, easy import to the functions for developing solutions in the future.

![PoseEstimation-Mediapipe gif](https://user-images.githubusercontent.com/61786557/143673861-b311e85c-dd15-4211-8494-4dd48e28a787.gif)

