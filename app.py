import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.set_page_config(page_title="Camera Capture App", layout="centered")

st.title("📸 Capture Image from Camera")

# Button to open the camera and capture image
capture_btn = st.button("Open Camera and Capture")

if capture_btn:
    # OpenCV captures from default webcam (0)
    cap = cv2.VideoCapture(0)
    st.info("Press 'c' to capture image and 'q' to quit.")

    captured_image = None

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access the camera.")
            break

        # Show the video frame using OpenCV window
        cv2.imshow("Camera - Press 'c' to capture, 'q' to quit", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("c"):
            captured_image = frame.copy()
            break
        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    if captured_image is not None:
        # Convert BGR (OpenCV) to RGB (PIL)
        img_rgb = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)
        st.image(img_rgb, caption="Captured Image", use_column_width=True)

        # Optionally save or process the image
        # cv2.imwrite("captured_image.jpg", captured_image)
