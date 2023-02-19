import cv2
import pytesseract
import datetime
import csv
from tkinter import *
from tkinter import simpledialog, messagebox

# set up the OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# set up the camera preview window
cap = cv2.VideoCapture(0)
cv2.namedWindow("AAES (Camera Preview)")

# get the lecture name from the user
root = Tk()
root.withdraw()
lecture_name = simpledialog.askstring("AAES (Automated Attendence Entry System)", "Enter the lecture name:")

# set up the CSV file with the lecture name and current date
date_string = datetime.datetime.now().strftime("%d-%m-%Y")
csv_filename = f"{lecture_name}_{date_string}.csv"

with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Enrollment Number", "Time"])

# set up a dictionary to store the last time an enrollment number was recorded
last_recorded = {}

# capture the image from the camera on space bar press
while True:
    ret, frame = cap.read()
    cv2.imshow("AAES (Camera Preview)", frame)

    if cv2.waitKey(1) == 32:
        # capture the image
        cv2.imwrite("icard.jpg", frame)

        # extract the enrollment number using OCR
        img = cv2.imread("icard.jpg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        result = 255 - opening
        enrollment_number = pytesseract.image_to_string(result, lang='eng', config='--psm 6')

        # remove any non-digit characters from the enrollment number
        enrollment_number = ''.join(filter(str.isdigit, enrollment_number))

        # check if the enrollment number has already been recorded within the last 30 minutes
        if enrollment_number in last_recorded and (datetime.datetime.now() - last_recorded[enrollment_number]).total_seconds() < 1800:
            print(f"Error, Enrollment number {enrollment_number} has already been recorded within the last 30 minutes.")
            messagebox.showerror("Error", f"Enrollment number {enrollment_number} has already been recorded within the last 30 minutes.")
        else:
            # record the enrollment number and current time in the CSV file
            with open(csv_filename, 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([enrollment_number, datetime.datetime.now().strftime("%H:%M:%S")])

            # update the last recorded time for the enrollment number
            last_recorded[enrollment_number] = datetime.datetime.now()

            # show a success message
            print(f"Success, Enrollment Number {enrollment_number} has been recorded")
            messagebox.showinfo("Success", f"Enrollment number {enrollment_number} has been recorded.")

    if cv2.getWindowProperty("AAES (Camera Preview)", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
