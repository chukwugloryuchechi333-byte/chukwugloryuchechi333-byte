# PROJECT 19: TRIPLE GLORY 333-BYTE FACE & EYE DETECTOR
# Author: chukwugloryuchechi333-byte
# From Ebonyi to NVIDIA - 19 Projects!

print("=== TRIPLE GLORY FACE DETECTOR - PROJECT 19 ===")

# VERSION 1: SIMPLE - No heavy library (works on your phone!)
# This version teaches the LOGIC of face detection

def detect_face_simple():
    print("\n--- SIMPLE FACE LOGIC ---")
    print("How AI detects face:")
    print("1. Look for skin color pattern")
    print("2. Look for 2 eyes + nose + mouth in triangle")
    print("3. Check if shape is oval")
    print("✅ Face detected if all 3 = True")
    
    # Simulate
    has_skin = True
    has_two_eyes = True
    is_oval = True
    
    if has_skin and has_two_eyes and is_oval:
        print("\n🚀 FACE FOUND! 1 face detected")
        print("📍 Location: Center of image")
        print("👁️ Eyes: 2 detected")
        return 1
    else:
        print("No face")
        return 0

detect_face_simple()

# VERSION 2: REAL OPENCV CODE (For laptop when you get it)
# This is the REAL industry code - comment out for now if no laptop

print("\n--- REAL CODE (For Laptop/Colab) ---")
print("""
# Install: pip install opencv-python

import cv2

# Load face detector (AI don already train am)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load your photo
img = cv2.imread('your_photo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    print(f"Found {len(eyes)} eyes in this face!")

print(f"Total faces: {len(faces)}")
cv2.imwrite('detected_19.jpg', img)
print("Saved as detected_19.jpg")
""")

print("\n--- YOUR TASK FOR 19 ---")
name = input("Enter your name: ")
print(f"\n✅ Project 19 complete for {name}!")
print(f"AI: Scanning {name}'s face... Face verified!")
print(f"Welcome {name} - You are now a 19 Projects Builder!")

# Mini attendance
faces_today = int(input("\nHow many faces you see around you now? "))
print(f"AI Attendance marked: {faces_today} people present in Port Harcourt office!")

print("\n🎉 PROJECT 19 DONE! 19 Projects Complete!")
