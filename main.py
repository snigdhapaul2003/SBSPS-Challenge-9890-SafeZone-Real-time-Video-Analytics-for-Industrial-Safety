import cv2
import torch
import numpy as np
import torch
from PIL import Image
from IPython.display import display, clear_output
import matplotlib.pyplot as plt

from ultralytics import YOLO
from playsound import playsound
import threading
audio_lock = threading.Lock()
def video_detection(path_x):
    model = YOLO("best.pt")
    video_capture = path_x
    video = cv2.VideoCapture(video_capture)


    # Define the polygonal ROI
    roi_points = np.array([[250, 720], [250, 400], [1020, 400], [1020, 720]], np.int32)

    # Define the actual dimensions of the object
    object_width = 50  # in centimeters

    # Define the focal length of the camera
    focal_length = 1000  # in pixels

    # Range of distance for CWS
    dist_ = 9
    c=0
    # Process each frame of the video
    while True:
        # Read the next frame
        success, frame = video.read()
        target_size = (1280, 720)
        frame = cv2.resize(frame, target_size)
        c=c+1
        print(c)
        if not success:
            break

        # Draw the polygonal ROI
        cv2.polylines(frame, [roi_points], True, (21, 21, 21), 2)

        # Calculate the y-coordinates of the three horizontal lines inside the ROI
        line_y1 = 550
        line_gap = 20
        line_ys = [line_y1 + i * line_gap for i in range(dist_)]

        # Initialize line colors and crossed line count
        line_colors = [(81, 196, 255) for _ in range(dist_)]
        crossed_lines = []
        # Perform object detection on the frame
        results = model(frame,stream=True)

        # Draw a dividing line in the center of the frame
        height, width, _ = frame.shape
        cv2.line(frame, (width // 2, 0), (width // 2, height), (160, 160, 160), 2)

        # Check whether the bounding box centroids are inside the ROI
        for r in results:
            boxes = r.boxes
            for box in boxes:
                xmin,ymin,xmax,ymax =box.xyxy[0]
                xmin,ymin,xmax,ymax =int(xmin),int(ymin),int(xmax),int(ymax)
                score = box.conf[0]
                class_id = box.cls[0]


                # Threshold score
                if score >= 0.4:

                    # Calculate the centroid coordinates
                    if xmin < frame.shape[1] // 2:
                        # Left side of the frame
                        centroid_x = int(xmax)
                        centroid_y = int(ymax)
                    else:
                        # Right side of the frame
                        centroid_x = int(xmin)
                        centroid_y = int(ymax)

                    # Check if the center of the bounding box is inside the polygon ROI
                    if cv2.pointPolygonTest(roi_points, (centroid_x, centroid_y), False) > 0:
                        cv2.circle(frame, (centroid_x, centroid_y), 5, (0, 255, 0), -1)

                        # Check if the bounding box touches any of the lines
                        for i, line_y in enumerate(line_ys):
                            if ymax >= line_y:
                                line_colors[i] = (0, 0, 255)  # Change line color to red
                                crossed_lines.append(i + 1)  # Add crossed line number to the list

                        # Calculate the distance to the object
                        distance = (object_width * focal_length) / (xmax - xmin)

                        # Draw the bounding box and display the distance
                        cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 2)
                        cv2.putText(frame, f"Dist: {distance:.2f} cm", (int(xmin), int(ymin) - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 255), 1)
                    else:
                        cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 2)



            for line_y, color in zip(line_ys, line_colors):
                cv2.line(frame, (roi_points[0][0], line_y), (roi_points[2][0], line_y), color, 2)

            # Print the crossed line numbers
            if crossed_lines:
                cv2.putText(frame, 'BRAKE', (1000 - 25, 100 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
                crossed_lines_str = ', '.join(str(line_num) for line_num in crossed_lines)
                # print(f"Crossed lines: {crossed_lines_str}")
                cv2.putText(frame, str(max(crossed_lines)), (1000 , 100 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

                if max(crossed_lines) >=2:
                    cv2.putText(frame, 'FORWARD COLLISION WARNING', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),
                                2, cv2.LINE_AA)
                    playsound('Emergency_Alarm.mp3')
                # elif max(crossed_lines) == 6 and max(crossed_lines) <= 8:
                #     cv2.putText(frame, 'COLLISION WARNING SEVERE', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2,
                #                 cv2.LINE_AA)
                #     playsound('Emergency_Alarm.mp3')
                # elif max(crossed_lines) >= 9 and max(crossed_lines) <= 11:
                #     cv2.putText(frame, 'PAY ATTENTION & TAKE CONTROL', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                #                 (0, 0, 255), 2, cv2.LINE_AA)
                #     playsound('Emergency_Alarm.mp3')
                # elif max(crossed_lines) >= 11:
                #     cv2.putText(frame, 'EMERGENCY STOPPING ..!!', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2,
                #                 cv2.LINE_AA)
                #     playsound('Emergency_Alarm.mp3')

        yield frame



cv2.destroyAllWindows()