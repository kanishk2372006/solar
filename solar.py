import cv2
import numpy as np

planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

solar_system_image = cv2.imread("solar-system.jpg")

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)  # White
font_thickness = 1

positions = [
    (40, 150), (180, 170), (290, 280), (400, 299),
    (600, 360), (820, 330), (970, 300), (1120, 370)
]

for i, name in enumerate(planet_names):
    position = positions[i]
    cv2.putText(solar_system_image, name, position, font, font_scale, font_color, font_thickness)

cv2.imshow("Solar System with Planet Names", solar_system_image)
cv2.waitKey(5000)

cv2.imwrite("solar_system_with_names.jpg", solar_system_image)
