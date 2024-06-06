# SafeZone: Real-time Video Analytics for Industrial Safety

---

## 📋 Problem Statement

**SafeZone**: Real-time Video Analytics for Industrial Safety

**Problem Description**: Industrial safety is essential for promoting worker safety, preventing accidents, ensuring compliance, and enhancing overall operational efficiency in industrial environments. By leveraging advanced video analytics technologies, we can offer a proactive and data-driven approach to industrial safety management.

Our goal is to develop a real-time video analytics tool that enhances industrial safety by detecting and preventing potential hazards and unsafe situations in industrial environments.

---

## 🚀 Chosen Solution

### AutoAware: Automatic Car Safety Alarm System

Our solution, **AutoAware**, aims to develop an advanced low-light object detection system using YOLOv8, a real-time object detection algorithm. Its core purpose is to enhance driver safety by identifying potential obstacles and hazards in low light conditions, specifically vehicles and pedestrians. The solution is versatile and applicable across logistics, delivery, construction, mining, and agriculture industries. Implementing the system on a driver's perspective video feed simulates real-world scenarios, offering practical safety enhancements for various transportation sectors.

---

## 📝 Requirement Analysis

### Functional Requirements

1. **Object Detection**: 
    - Custom YOLOv8 model trained for real-time detection of pedestrians and cars within video streams.
    - Detected objects are displayed with bounding boxes on the video frames.
2. **Video Sources**:
    - Supports both live webcam feeds and uploaded video files as input sources.
3. **Alarm System**: 
    - Integrated alarm system promptly alerts drivers upon detection of obstacles within the designated region of interest.
4. **User Interface**: 
    - Presents live video feed with bounding boxes around identified obstacles.
    - Highlights predefined ROI and provides clear indicators when obstacles enter this area.
    - Auditory alerts are accompanied by corresponding visual cues on the interface.

### Environmental Requirements

- **Hardware**:
  - Minimum processor specs: i3 6th gen
  - Minimum 4 GB RAM
  - Intel integrated graphics
  - Minimum 10 GB disk space
  - Webcam

- **Software**:
  - Python 3.8 or higher
  - Required libraries: Flask, OpenCV, playsound, torch, ultralytics, etc.
  - Compatible web browsers: Chrome, Firefox, Safari, Microsoft Edge
  - Operating System: Windows 7 or higher (recommended)

### Constraints and Future Enhancements

1. **Integration with Vehicle Systems**: Potential integration with existing vehicle monitoring and driver assistance technologies.
2. **Multi-Camera Support**: Expanding capabilities to encompass multiple camera feeds for a comprehensive view.
3. **Machine Learning Improvements**: Continuous research and improvements to the YOLOv8 algorithm to enhance accuracy and efficiency.

---

## ⚙️ System Specification

### Live Webcam-based Object Detection

- **Bounding Boxes**: Detected objects are marked with bounding boxes directly overlaid on the live video feed.
- **Region of Interest (ROI)**: A predefined ROI within the video frame is monitored for obstacle entry. Visual cues highlight objects entering this area.
- **Real-Time Feedback**: Provides instant feedback about obstacles and hazards as they emerge in the webcam's view.

### Detection based on Uploaded Video File

Allows users to analyze pre-recorded videos for object detection and hazard assessment. Users can upload video files and receive insights about potential obstacles in low light conditions.

### Vehicle Collision Alerting System

- **Auditory and Visual Alerts**: Alerts draw the driver's attention to potential collision risks, helping them remain focused on the road and surroundings.

---

## 🛠️ Technology Stack

### Front-End

- **HTML**: Structures the user interface and defines the layout.
- **CSS**: Styles the user interface, applying visual aesthetics for a pleasant experience.
- **JavaScript**: Creates dynamic interactions, handles user inputs, and enhances engagement.

### Back-End

- **Flask**: Manages server-side functions and connects the front-end with the back-end.
- **Python**: Orchestrates various components, libraries, and functionalities for real-time object detection, user interface management, deep learning model implementation, and audio feedback.
- **PyTorch**: Implements and trains the YOLOv8 object detection algorithm.
- **IBM Watson Machine Learning**: Converts object labels into the YOLO format for effective training, ensuring accurate detection and localization of objects in low light conditions.
- **YOLOv8**: Custom model training process using the ExDark dataset, achieving a mAP value of nearly 70%.
- **OpenCV**: Instrumental for image and video processing.
  - **Webcam Feed Capture**: Captures live video feeds from the webcam.
  - **Frame Processing**: Processes individual video frames for object detection and hazard assessment.
  - **Object Detection Visualization**: Draws bounding boxes around detected objects.
  - **ROI Monitoring**: Defines and monitors a predefined ROI within video frames.
- **Playsound**: Generates auditory alerts to provide immediate audio cues to the driver.

---

## 🖥️ System Setup

1. **Create Virtual Environment**: Set up a virtual environment using a tool like PyCharm to isolate project dependencies.
2. **Clone Repository**: Clone the project's GitHub repository to a local directory within the virtual environment.
3. **Navigate to Project Directory**: Use the terminal/command prompt to navigate to the project directory.
4. **Install Dependencies**: Run `pip install -r requirements.txt` to install the required Python libraries and dependencies.
5. **Run the Web App**: Execute the `app.py` file by running the command `python app.py` in the terminal.
6. **Access the Web App**: Open a web browser and enter the provided URL (usually `http://localhost:5000`) to access the web app.

This setup allows you to interact with the low-light object detection system and experience its features firsthand.

---

## 🙏 Acknowledgements

We extend our sincere gratitude to **IBM** for their support and resources that have greatly contributed to the success of this project. The opportunity to work with their cutting-edge technologies and platforms has been invaluable.

We would also like to express our heartfelt appreciation to all the guides and mentors who have been instrumental in guiding us throughout the project's development. Their insights, expertise, and unwavering support have been crucial in shaping the project and achieving its objectives.

We acknowledge the collaborative efforts of our fellow team members who have worked diligently to bring this project to fruition. Each contribution, no matter how small, has played a significant role in the project's overall success.

Finally, we thank our families, friends, and colleagues for their understanding, encouragement, and motivation throughout this journey. Your support has been the cornerstone of our progress.

---

*Thank you for exploring our project. We hope it contributes to enhancing safety and operational efficiency in various industrial environments.*





DEMO VIDEO LINK: https://youtu.be/kjz53xUkTqs


TEAM MEMBERS: 

              SRIJA CHAKRABORTY
              SAMBIT MALLICK 
              SNIGDHA PAUL
