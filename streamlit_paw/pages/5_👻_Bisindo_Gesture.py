import os
import cv2
import streamlit as st
from streamlit_navigation_bar import st_navbar
from PIL import Image
import numpy as np
import tensorflow as tf

st.set_page_config(
    page_title="Bisindo Gesture - Streamlit App",
    page_icon="🔥",
    initial_sidebar_state="collapsed",
)

styles = {
    "nav": {
        "background-color": "royalblue",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "border-radius": "0.5rem",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
options = {
    "show_sidebar": False,
}

page = st_navbar(["Home", "Statistics", "Calculation", "Sentiment Analysis",
                 "Regression", "Image Classification", "About"], selected="Image Classification", styles=styles, options=options)

if page == "Home":
    st.switch_page("0_🏠_Home.py")
if page == "Statistics":
    st.switch_page("pages/1_📊_Statistics.py")
if page == "Calculation":
    st.switch_page("pages/2_🔢_Calculation.py")
if page == "Sentiment Analysis":
    st.switch_page("pages/3_😶_Sentiment_Analysis.py")
if page == "Regression":
    st.switch_page("pages/4_📈_Linear_Regression.py")
if page == "About":
    st.switch_page("pages/6_🔣_About.py")



@st.cache_resource
def load_model(model_file):
    interpreter = tf.lite.Interpreter(model_path=os.path.join(
        'streamlit_paw/models', model_file))
    interpreter.allocate_tensors()
    return interpreter


def detect_gesture(camera_img, interpreter, labels, min_conf=0.5):
    # Get model details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    input_height = input_details[0]['shape'][1]
    input_width = input_details[0]['shape'][2]
    float_input = (input_details[0]['dtype'] == np.float32)

    input_mean = 127.5
    input_std = 127.5

    # Preprocess the image
    image = np.array(camera_img)  # Convert PIL image to numpy array
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imH, imW, _ = image.shape

    # Resize and normalize the image
    image_resized = cv2.resize(image_rgb, (input_width, input_height))
    input_data = np.expand_dims(image_resized, axis=0).astype(np.float32)

    # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
    if float_input:
        input_data = (np.float32(input_data) - input_mean) / input_std

    # Perform detection
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Retrieve detection results
    boxes = interpreter.get_tensor(output_details[1]['index'])[0]
    classes = interpreter.get_tensor(output_details[3]['index'])[0]
    scores = interpreter.get_tensor(output_details[0]['index'])[0]

    # Draw detections on the image
    for i in range(len(scores)):
        if (scores[i] > min_conf) and (scores[i] <= 1.0):
            ymin = int(max(1, (boxes[i][0] * imH)))
            xmin = int(max(1, (boxes[i][1] * imW)))
            ymax = int(min(imH, (boxes[i][2] * imH)))
            xmax = int(min(imW, (boxes[i][3] * imW)))

            # Draw bounding box and label on image
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (10, 255, 0), 2)

            # Draw label
            object_name = labels[int(classes[i])] # Look up object name from "labels" array using class index
            label = '%s: %d%%' % (object_name, int(scores[i]*100)) # Example: 'person: 72%'
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
            label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of window
            cv2.rectangle(image, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
            cv2.putText(image, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # Draw label text

    # Convert back to RGB for display in Streamlit
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

st.title(":ghost: Bisindo Gesture")

# Load model and labels
labels = [line.strip() for line in open(os.path.join(
    'streamlit_paw/models', "ssd_mobilenet_v2_bisindo_label.txt")).readlines()]
model = load_model("ssd_mobilenet_v2_bisindo.tflite")

image = st.camera_input("Take a picture")

if image:
    img = Image.open(image)
    result_img = detect_gesture(img, model, labels, min_conf=0.5)
    st.image(result_img, caption="Detection Results", use_column_width=True)
