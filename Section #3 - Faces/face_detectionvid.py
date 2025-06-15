import cv2 as cv

# Load Haar cascade only once
haar_cascade = cv.CascadeClassifier("haar_cascade.xml")

# Open webcam
vid = cv.VideoCapture(0)

while True:
    isTrue, frame = vid.read()

    if not isTrue:
        print("Failed to grab frame.")
        break

    # Detect faces
    face_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=9)
    print(f'Number of faces: {len(face_rect)}')

    # Draw rectangles around faces
    for (x, y, w, h) in face_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    # Show the frame with rectangles
    cv.imshow("Detected Faces", frame)

    # Break on pressing 'd'
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release resources
vid.release()
cv.destroyAllWindows()
