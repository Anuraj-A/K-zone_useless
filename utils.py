import cv2
import numpy as np

def classify_pothole(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return "No pothole detected"

    largest_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest_contour)
    perimeter = cv2.arcLength(largest_contour, True)

    # Simple rules (tweak values based on testing)
    if area < 1500:
        return "Challenger"
    elif area < 4000:
        return "Tyre-Guzzler"
    elif area < 8000 or perimeter > 300:
        return "Suspension Smasher"
    else:
        return "The Great Keralan Abyss"
