import cv2

def extract_frame(video_path, frame_output_path):
    # Open the video
    video = cv2.VideoCapture(video_path)

    # Get the number of total frames in the vieo
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Variables for mouse clicking to be used for video image saving
    clicked_x = None
    clicked_y = None

    def mouse_callback(event, x, y, flags, param):
        nonlocal clicked_x, clicked_y
        if event == cv2.EVENT_LBUTTONDOWN:
            clicked_x = x
            clicked_y = y

    # Create window for video browsing
    cv2.namedWindow("Video Player")
    cv2.setMouseCallback("Video Player", mouse_callback)

    # Video playback
    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Show the image
        cv2.imshow("Video Player", frame)

        # Waiting for a mouse click (choosing video frame) or "q" key to exit
        key = cv2.waitKey(1000) & 0xFF  # Waiting time in ms
        if key == ord('q'):
            break
        elif clicked_x is not None and clicked_y is not None:
            # Save chosen image
            cv2.imwrite(frame_output_path, frame)
            print("Snímek uložen.")
            break

    # Close the video and the window
    video.release()
    cv2.destroyAllWindows()

# Path to the video
video_path = "/path/video.mp4"

# Output image path
frame_output_path = "/Desktop/image_output.jpg"

# Video frame as an image extraction
extract_frame(video_path, frame_output_path)
