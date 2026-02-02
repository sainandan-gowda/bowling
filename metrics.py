import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("keypoints1.csv")


# Helper function to calculate angle

def calculate_angle(a, b, c):
    """
    Calculate angle at point b using points a-b-c
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (
        np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6
    )
    angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))
    return angle


# METRIC 1: Knee Angle
# Right side: Hip(23), Knee(25), Ankle(27)

knee_angles = []

for _, row in df.iterrows():
    hip = (row["x_23"], row["y_23"])
    knee = (row["x_25"], row["y_25"])
    ankle = (row["x_27"], row["y_27"])
    knee_angles.append(calculate_angle(hip, knee, ankle))

avg_knee_angle = np.mean(knee_angles)


# METRIC 2: Elbow Angle
# Right arm: Shoulder(12), Elbow(14), Wrist(16)

elbow_angles = []

for _, row in df.iterrows():
    shoulder = (row["x_12"], row["y_12"])
    elbow = (row["x_14"], row["y_14"])
    wrist = (row["x_16"], row["y_16"])
    elbow_angles.append(calculate_angle(shoulder, elbow, wrist))

avg_elbow_angle = np.mean(elbow_angles)


# METRIC 3: Stability Score
# Hip movement variance

stability_score = np.var(df["x_23"]) + np.var(df["y_23"])


# Print results

print("===== BIOMECHANICAL METRICS =====")
print(f"Average Knee Angle (deg): {avg_knee_angle:.2f}")
print(f"Average Elbow Angle (deg): {avg_elbow_angle:.2f}")
print(f"Stability Score (lower is better): {stability_score:.6f}")


#  PLOTS


# Knee angle over time
plt.figure()
plt.plot(knee_angles)
plt.xlabel("Frame")
plt.ylabel("Knee Angle (degrees)")
plt.title("Knee Angle Over Time")
plt.show()

# Elbow angle over time
plt.figure()
plt.plot(elbow_angles)
plt.xlabel("Frame")
plt.ylabel("Elbow Angle (degrees)")
plt.title("Elbow Angle Over Time")
plt.show()

# Hip trajectory (stability visualization)
plt.figure()
plt.plot(df["x_23"], df["y_23"])
plt.xlabel("Hip X Position")
plt.ylabel("Hip Y Position")
plt.title("Hip Movement Trajectory")
plt.show()
