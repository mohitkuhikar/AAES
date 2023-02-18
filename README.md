# AAES
Project Title: Enrollment-based Attendance System

Project Description:
This project aims to create an automated attendance system using Python programming language. The system reads the enrollment number from an ID card and checks it against a list of student enrollments for a particular class. If the enrollment number matches a student's enrollment, the system records the student's attendance in a CSV file. If the enrollment number does not match any student's enrollment, the system displays a message indicating that the student does not belong to the class.

The system uses the following tools and technologies:

Python programming language
OpenCV library for capturing images from a camera
Tesseract OCR library for recognizing text in images
pandas library for reading and writing CSV files
Regular expressions for extracting enrollment numbers from text
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
