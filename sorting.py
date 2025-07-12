import torch
from PIL import Image
import cv2
import RPi.GPIO as GPIO
import time
from torchvision import transforms

# ----- GPIO Setup -----
GPIO.setmode(GPIO.BCM)
RIGHT_PIN = 17  # Fresh
LEFT_PIN = 27   # Stale
GPIO.setup(RIGHT_PIN, GPIO.OUT)
GPIO.setup(LEFT_PIN, GPIO.OUT)

# ----- Class Labels -----
class_names = ['fresh', 'stale']

# ----- Load Model -----
model = torch.load('/home/pi/model/capsicum_model.pth', map_location=torch.device('cpu'))
model.eval()

# ----- Image Preprocessing -----
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# ----- Camera Setup -----
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Display live frame
        cv2.imshow('frame', frame)

        # Convert to PIL and preprocess
        img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img_tensor = transform(img_pil).unsqueeze(0)

        # Prediction
        with torch.no_grad():
            output = model(img_tensor)
            _, pred = torch.max(output, 1)
            prediction = class_names[pred.item()]
            print(prediction, output)

        # Motor control logic
        if prediction == 'fresh':
            GPIO.output(RIGHT_PIN, GPIO.HIGH)
            time.sleep(1.5)  # run conveyor right
            GPIO.output(RIGHT_PIN, GPIO.LOW)
        else:  # stale
            GPIO.output(LEFT_PIN, GPIO.HIGH)
            time.sleep(1.5)  # run conveyor left
            GPIO.output(LEFT_PIN, GPIO.LOW)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
