import cv2 as cv #type:ignore
import mediapipe.python.solutions.hands as mp_hands # type: ignore
import mediapipe.python.solutions.drawing_utils as drawing # type: ignore
import mediapipe.python.solutions.drawing_styles as drawing_styles # type: ignore


hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands = 1,
    min_detection_confidence =0.5,

)
VIDEO_WIDTH = 400
VIDEO_HEIGHT = 200
cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, VIDEO_WIDTH)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, VIDEO_HEIGHT)



while cam.isOpened():
    success, frame = cam.read()
    if not success:
        print("Camera frame not available")
        continue

    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    hands_detected = hands.process(frame)

    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    if( hands_detected.multi_hand_landmarks):
        for hand_landmarks in hands_detected.multi_hand_landmarks:

            drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style()

            )



            normalizedLandmark = hand_landmarks.landmark[0].x
    
            print(normalizedLandmark)

    cv.imshow("Show video",frame)
    

    if (cv.waitKey(20) & 0xff == ord('q')):
        break

cv.destroyAllWindows()
cam.release()

