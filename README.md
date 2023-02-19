# AAES
Project Title: AUTOMATED ATTENDENCE ENTRY SYSTEM (Enrollment-based Attendance System)

Project Description:

This project aims to create an automated attendance system using Python programming language. The system reads the enrollment number from an ID card and checks it against a list of student enrollments for a particular class. If the enrollment number matches a student's enrollment, the system records the student's attendance in a CSV file. If the enrollment number does not match any student's enrollment, the system displays a message indicating that the student does not belong to the class.

The system uses the following tools and technologies:

* Python programming language
* OpenCV library for capturing images from a camera
* Tesseract OCR library for recognizing text in images
* pandas library for reading and writing CSV files
* Regular expressions for extracting enrollment numbers from text

The project can be implemented by following these steps:

1. Set up the camera to capture images
2. Load the list of student enrollments for the class from a CSV file
3. Create a CSV file for recording attendance
4. Start a loop to capture images from the camera
5. Pre-process the captured image to improve text recognition
6. Use Tesseract OCR to recognize text in the image
7. Extract the enrollment number from the text using regular expressions
8. Check if the enrollment number matches any student's enrollment in the class
9. If there is a match, record the attendance by adding a new row to the CSV file
10. If there is no match, display a message indicating that the student does not belong to the class
11. Display the camera feed
12. Exit the loop on pressing the escape key

With this project, we can automate the attendance process and eliminate the need for manual recording of attendance. It can also reduce errors and save time.

Automated Attendance Entry System (AAES) is a Python script that uses Optical Character Recognition (OCR) and a webcam to automate the process of taking attendance in a classroom or lecture hall. The script captures an image of an identity card, extracts the enrollment number from the card using OCR, and records the enrollment number and current time in a CSV file.

The script uses the following tools and libraries:

* OpenCV (cv2): an open-source computer vision library for image and video processing.
* PyTesseract: a Python wrapper for Google's Tesseract-OCR engine that provides OCR capabilities.
* datetime: a Python module that provides classes for working with dates and times.
* csv: a Python module for working with CSV files.
* tkinter: a Python GUI toolkit for creating windows and dialog boxes.

Here are the steps to implement the AAES system:

1. Install the required tools and libraries (OpenCV, PyTesseract, datetime, csv, and tkinter).
2. Set up the OCR engine by providing the path to the Tesseract-OCR executable.
3. Set up a camera preview window using the OpenCV namedWindow function.
4. Prompt the user to enter the lecture name using a tkinter simpledialog box.
5. Create a CSV file with the lecture name and current date, and write the header row.
6. Set up a dictionary to store the last time an enrollment number was recorded.
7. Enter a loop that captures images from the webcam and displays them in the preview window.
8. When the space bar is pressed, capture the current image and extract the enrollment number from it using PyTesseract.
9. Check if the enrollment number has already been recorded within the last 30 minutes, and display an error message if it has.
9. If the enrollment number has not been recorded within the last 30 minutes, record it and the current time in the CSV file, and update the dictionary with the current time.
10. Display a success message to the user.
11. Repeat the loop until the preview window is closed.

Overall, the AAES system provides a simple and automated way to take attendance in a classroom or lecture hall, saving time and reducing the risk of errors that can occur with manual entry.
