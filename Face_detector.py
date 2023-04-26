import cv2

# # Start the webcam
# cap = cv2.VideoCapture(0)

# # Load the cascade
# face_cascade = cv2.CascadeClassifier('opencvfile.xml')

# while True:
#     # Read the frame
#     _, frame = cap.read()

#     # Convert to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect the faces
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#     # Draw the rectangle around each face
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#     # Display the output
#     cv2.imshow('face detection', frame)

#     # Check if the user pressed 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam
# cap.release()
# cv2.destroyAllWindows()


# Start the webcam
cap = cv2.VideoCapture(0)

# Set the width and height of the frames in the video file
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

# Load the cascade
face_cascade = cv2.CascadeClassifier('opencvfile.xml')

while True:
    # Read the frame
    _, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Write the frame to the video file
    out.write(frame)

    # Display the output
    cv2.imshow('face detection', frame)

    # Check if the user pressed 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and video writer
cap
