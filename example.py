import cv2
import pytesseract
import re
import pandas as pd
from datetime import date

# Initialize camera
cam = cv2.VideoCapture(0)

# Set up Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load CSV file of student enrollments
class_enrollments = pd.read_csv('class_enrollments.csv')

# Load CSV file of attendance records
attendance_file = 'attendance_' + str(date.today()) + '.csv'

# Initialize attendance record DataFrame
if attendance_file not in os.listdir():
    attendance = pd.DataFrame(columns=['Enrollment', 'Time'])
else:
    attendance = pd.read_csv(attendance_file)

# Start camera capture loop
while True:
    # Capture image from camera
    ret, frame = cam.read()
    
    # Pre-process image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    
    # Use Tesseract OCR to recognize text
    text = pytesseract.image_to_string(gray)
    
    # Extract enrollment number using regular expressions
    match = re.search(r"Enrollment:\s*(\d*)", text)
    if match:
        enrollment = match.group(1)
        
        # Check if person belongs to class
        if enrollment in class_enrollments['Enrollment'].values:
            # Add attendance record
            attendance = attendance.append({'Enrollment': enrollment, 'Time': str(date.today())}, ignore_index=True)
            attendance.to_csv(attendance_file, index=False)
            
            # Display attendance information
            print('Attendance recorded for enrollment number', enrollment)
        else:
            print('You do not belong to this class')
    
    # Show camera feed
    cv2.imshow('Camera', frame)
    
    # Exit on escape key press
    if cv2.waitKey(1) == 27:
        break

# Release camera and close window
cam.release()
cv2.destroyAllWindows()


***This updated code only reads the enrollment number from the ID card and checks it against the list of enrollments for the class. It then records the attendance of the student with that enrollment number and adds a new record to the attendance DataFrame. Finally, it displays a message indicating whether the attendance was recorded or not. Note that this code assumes that the ID cards have a specific format that includes the enrollment number in a specific location. If the ID cards have a different format, we may need to modify the regular expression used to extract the enrollment number.***
