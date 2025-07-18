import cv2
import numpy as np
import mediapipe as mp
import time

# Initialize MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

# Create a black sketch canvas
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# To store previous finger positions for shaking detection
prev_x, prev_y = 0, 0
shake_counter = 0
shake_threshold = 25  # Pixels
shake_detected = False

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)  # Mirror the image
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Index finger tip (landmark 8)
            x = int(hand_landmarks.landmark[8].x * 640)
            y = int(hand_landmarks.landmark[8].y * 480)

            # Draw circle at fingertip
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

            # Finger shaking detection
            if abs(x - prev_x) > shake_threshold:
                shake_counter += 1
            else:
                shake_counter = max(0, shake_counter - 1)

            if shake_counter > 5:
                shake_detected = True
                cv2.putText(frame, "Shaking Detected!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 3)
            else:
                shake_detected = False

            # Draw on canvas if not shaking
            if not shake_detected and prev_x != 0 and prev_y != 0:
                cv2.line(canvas, (prev_x, prev_y), (x, y), (255, 255, 255), 5)

            prev_x, prev_y = x, y

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Overlay the canvas on webcam feed
    combined = cv2.add(frame, canvas)

    cv2.imshow("Finger Shake Sketch", combined)
    key = cv2.waitKey(1)
    if key == ord('c'):  # Clear canvas
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)
    elif key == 27:  # ESC key to quit
        break

cap.release()
cv2.destroyAllWindows()
