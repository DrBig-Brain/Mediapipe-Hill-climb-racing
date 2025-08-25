import cv2
import mediapipe as mp
import pydirectinput

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

# Main loop
while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    right_hand_up = False
    left_hand_up = False

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):

            # Get bounding box
            h, w, _ = img.shape
            x_coords = [lm.x for lm in hand_landmarks.landmark]
            y_coords = [lm.y for lm in hand_landmarks.landmark]

            x_min = int(min(x_coords) * w)
            x_max = int(max(x_coords) * w)
            y_min = int(min(y_coords) * h)
            y_max = int(max(y_coords) * h)

            # Draw bounding box
            label = handedness.classification[0].label  # 'Left' or 'Right'
            cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 255), 2)
            cv2.putText(img, f"{label} Hand", (x_min, y_min - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

            # Gesture detection (middle finger tip vs wrist)
            wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
            middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y

            if middle_tip_y < wrist_y:  # Hand is up
                if label == 'Right':
                    right_hand_up = True
                elif label == 'Left':
                    left_hand_up = True

    # Control game
    if left_hand_up:
        pydirectinput.keyDown('right')
    else:
        pydirectinput.keyUp('right')

    if right_hand_up:
        pydirectinput.keyDown('left')
    else:
        pydirectinput.keyUp('left')

    # Show webcam feed
    cv2.imshow("Gesture Control", img)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
