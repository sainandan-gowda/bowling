import cv2
import mediapipe as mp
import pandas as pd
import numpy as np


mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    enable_segmentation=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Open input video
cap = cv2.VideoCapture("input1.mp4")

if not cap.isOpened():
    print(" Error: Video not found")
    exit()


output_width = 960
output_height = 540
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    "skeleton_output.mp4",
    fourcc,
    fps,
    (output_width, output_height)
)

keypoints_data = []
frame_no = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (output_width, output_height))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        row = {"frame": frame_no}
        for idx, lm in enumerate(results.pose_landmarks.landmark):
            row[f"x_{idx}"] = lm.x
            row[f"y_{idx}"] = lm.y
            row[f"z_{idx}"] = lm.z
            row[f"v_{idx}"] = lm.visibility

        keypoints_data.append(row)

   
    out.write(frame)

    cv2.imshow("Bowling Pose Estimation", frame)
    if cv2.waitKey(1) & 0xFF == 27:  
        break

    frame_no += 1

cap.release()
out.release()   
cv2.destroyAllWindows()

df = pd.DataFrame(keypoints_data)
df.to_csv("keypoints1.csv", index=False)

print(" Pose estimation complete")
print(" Keypoints saved as keypoints1.csv")
print(" Skeleton output video saved as skeleton_output.mp4")
