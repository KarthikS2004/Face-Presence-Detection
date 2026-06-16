# Face-Presence-Detection
# Task Overview

## Face Presence Detection 

A real-time face presence monitoring system that continuously detects whether a candidate remains visible during an online interview session.

The system uses computer vision techniques to detect faces, monitor candidate presence, calculate absence duration, and generate structured JSON output. It also provides an API endpoint for external systems to retrieve the latest monitoring status.

This project demonstrates real-time face detection, presence tracking, state management, API integration, and interview monitoring workflow implementation.

---

# Features

* Real-time face detection
* Continuous presence monitoring
* Candidate absence detection
* Absence duration tracking
* Configurable absence threshold
* JSON status output
* Timestamp generation
* REST API integration
* Video sample testing support
* Low-latency monitoring

---

# Problem Statement

During online interviews and assessments, candidates are expected to remain visible within the camera frame. Manual monitoring is inefficient and prone to errors.

The objective of this project is to automatically detect whether a candidate is present, track periods of absence, and provide real-time monitoring information that can be integrated into interview management systems.

---

# System Architecture

```text
Camera / Video Feed
          │
          ▼
    Frame Capture
          │
          ▼
   Face Detection
    (OpenCV Haar Cascade)
          │
          ▼
   Face Present?
      ┌─────┴─────┐
      │           │
     Yes          No
      │           │
      ▼           ▼
 Reset Timer   Start Timer
      │           │
      └─────┬─────┘
            ▼
 Generate JSON Output
            │
            ▼
       Flask API
```

---

# Technologies Used

## Programming Language

* Python 3

## Libraries

* OpenCV
* Flask
* JSON
* Time

## Tools

* Visual Studio Code
* Jupyter Notebook
* GitHub

---

# Project Workflow

1. System captures frames from webcam or video source.
2. Frames are converted to grayscale.
3. Histogram equalization improves detection under low-light conditions.
4. OpenCV Haar Cascade detects faces.
5. Face presence status is evaluated.
6. Absence timer starts when no face is detected.
7. If absence exceeds threshold, candidate is marked absent.
8. JSON output is generated with timestamp.
9. Flask API provides real-time access to monitoring status.

---

# Example Output

```json
{
  "face_present": false,
  "duration_absent_sec": 3.15,
  "timestamp": "2025-06-16 18:30:45"
}
```
Video Sample Testing

The Face Presence Detection system was validated using multiple recorded video samples to ensure reliable performance under different interview monitoring scenarios.

Test Case 1 – Face Present
Scenario

Candidate remained visible throughout the video session.

Output
{
  "face_present": true,
  "duration_absent_sec": 0,
  "timestamp": "2025-06-16 18:20:15"
}
Result

Passed ✅

### API Response

```json
{
  "face_present": true,
  "duration_absent_sec": 0,
  "timestamp": "2025-06-16 18:35:12"
}
```

---

# Results

* Successfully detected candidate presence in real time.
* Tracked absence duration accurately.
* Generated JSON-based monitoring output.
* Implemented configurable threshold handling.
* Reduced false absence detection using timer-based validation.
* Successfully integrated REST API endpoint.
* Demonstrated real-time monitoring capability using webcam and video samples.
* Improved interview monitoring automation.

---

# Skills Demonstrated

* Python Programming
* Computer Vision
* OpenCV
* Face Detection
* Real-Time Processing
* State Management
* REST API Development
* Flask
* Debugging
* Software Development

---

# Future Enhancements

* MediaPipe-based face detection
* Multi-face monitoring support
* Face recognition integration
* Attendance analytics dashboard
* Cloud deployment
* Real-time alert notifications
* Advanced occlusion handling
* Interview session reporting

---

# About Me

## Author

Karthik.S


### Skills

* Python
* SQL
* OpenCV
* Flask
* Java
* Data Analysis

### GitHub

https://github.com/KarthikS2004
