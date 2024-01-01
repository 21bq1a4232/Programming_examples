import cv2
def capture_image():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Unable to access the camera.")
        return
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture image.")
    else:
        cv2.imshow("Captured Image", frame)
        cv2.waitKey(0)
        image_file = "captured_image.jpg"
        # path of this script
        directory = "C:\Users\prana\OneDrive\Desktop\resume\"

# get fileName from user
        filepath = directory + image_file
        with open(filepath, 'w+') as fp:
            pass

# Creates a new file
        cv2.imwrite(image_file, frame)
        print(f"Image saved as {image_file}")
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()