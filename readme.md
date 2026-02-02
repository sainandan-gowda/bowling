# AI/ML Computer Vision – Sports Biomechanics Assignment

## Overview
This project focuses on analyzing a cricket bowling action using pose estimation and basic biomechanics principles.
The analysis was performed on a screen-recorded side-view cricket video, and the goal was to move beyond pose visualization to extract meaningful movement metrics that describe the player’s technique.

---

## Step 1: Video Selection
A side-view cricket bowling video obtained through screen recording was selected for this analysis.
This angle(side-view) is suitable because it clearly shows lower-body movement, arm action, and overall body balance during the bowling delivery.

However, fast arm motion and partial occlusion by the bowling arm can sometimes affect pose accuracy. Additionally, the screen-recorded nature of the video may slightly reduce visual quality, which was taken into consideration during the analysis.

---

## Step 2: Pose Estimation
MediaPipe Pose was used as the pose estimation model.  
It is lightweight, easy to use, and performs well for single-person sports videos without requiring any training.

Using MediaPipe, frame-wise body keypoints were extracted and a skeleton overlay was generated to visually verify the accuracy of pose detection.  
The extracted keypoints were stored in a CSV file for further analysis.

---

## Step 3: Movement Metrics (Core Analysis)

After extracting the pose keypoints, three meaningful biomechanics metrics were defined and analyzed to better understand the bowling action. The focus here was to move beyond pose visualization and translate joint movements into interpretable performance indicators.

### 1. Knee Angle
The knee angle was calculated using the hip, knee, and ankle keypoints.  
This metric helps capture how the lower body contributes to balance and force generation during the bowling action, while also giving insight into potential injury risk.

The results showed controlled knee flexion during the delivery phase, suggesting a stable lower-body posture that supports effective movement and balance.

---

### 2. Elbow Angle
The elbow angle was calculated using the shoulder, elbow, and wrist keypoints of the bowling arm.  
This metric is useful for analyzing arm extension and overall bowling technique efficiency.

For most frames, the elbow remained close to full extension, indicating an efficient and well-controlled arm action. Sudden drops in the angle were mainly caused by fast arm movement and minor pose estimation jitter.

---

### 3. Stability Score
A stability score was computed using the variance of hip joint movement across frames.  
This metric provides a simple way to estimate overall body balance during the bowling action.

The low stability score observed in the results suggests that the player maintained good control and balance throughout the motion, with limited unnecessary body movement.

---

### Metrics Output Summary

The extracted biomechanics metrics from the bowling video are summarized below:

- **Average Knee Angle:** 146.55°  
  This indicates moderate knee flexion during the bowling action, which helps maintain balance and contributes to effective force generation.

- **Average Elbow Angle:** 148.93°  
  The elbow stays close to full extension for most of the delivery, suggesting an efficient and controlled bowling arm action. Minor variations are mainly due to fast motion and pose estimation noise.

- **Stability Score:** 0.00589 (lower is better)  
  The low stability score indicates minimal hip movement variation, reflecting good overall body balance and control during the bowling motion.

Overall, these metrics demonstrate how pose keypoints can be converted into meaningful insights about bowling technique, rather than being used only for visual skeleton overlays.


## Step 4: Model Improvement Thinking

### Observed Issues
- Minor jitter in wrist keypoints during fast arm movement  
- Occasional inaccuracies due to occlusion and single camera view  
- Depth estimation limitations from a 2D video  

---

### Future Improvements
If more time and data were available, the following improvements could be made:
- Collect cricket-specific pose data for fine-tuning  
- Apply temporal smoothing techniques to reduce jitter  
- Use higher frame-rate videos for better motion capture  

---

### Data Collection Strategy
Data would be collected from:
- Multiple bowlers  
- Different bowling speeds  
- Left- and right-handed players  
- Various lighting conditions and backgrounds  

---

### Train / Validation / Test Split
The dataset would be split as follows:
- 70% Training  
- 15% Validation  
- 15% Testing  

This ensures proper generalization and avoids overfitting.

---

### Evaluation Method
Model improvements would be evaluated by:
- Reduced keypoint jitter  
- Smoother joint angle curves  
- More consistent metrics across repeated bowling actions  

---

## Conclusion
This project demonstrates how pose estimation can be converted into interpretable biomechanics insights using simple techniques.  
Rather than focusing on perfect accuracy, the emphasis was on understanding movement, identifying limitations, and thinking about real-world improvements for sports performance analysis.
