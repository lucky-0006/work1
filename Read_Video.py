# The code is using the OpenCV library in Python to capture video from a webcam or a video file.
import cv2

#Use 0 for webcam
vid = cv2.VideoCapture(0)

# `vid = cv2.VideoCapture("AnthonyShkraba.mp4")` is creating a `VideoCapture` object named `vid` that
# will read video frames from the file "AnthonyShkraba.mp4". This line of code is used to open and
# read a video file instead of capturing video from a webcam.
#vid = cv2.VideoCapture("C:/Users/HP/Desktop/python/C105/AnthonyShkraba.mp4")

# The code `if(vid.isOpened()==False): print("Unable to read the feed")` is checking if the video
# capture object `vid` is able to open and read the video feed. If the video feed cannot be opened, it
# will print the message "Unable to read the feed".
if(vid.isOpened()==False):
    print("Unable to read the feed")


# The code is using the `vid.get()` function from the OpenCV library to retrieve the properties of the
# video being captured or read.
height  = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

# The line `out = cv2.VideoWriter('Boxing.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))`
# is creating a `VideoWriter` object named `out` that will write video frames to a file named
# "Boxing.mp4".
out = cv2.VideoWriter('webcamfeed.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

# The `while(True)` loop is used to continuously capture video frames from the webcam or video file.
# The `while(True)` loop is used to continuously capture video frames from the webcam or video file.
while(True):
      
    # Capture the video frame
    # by frame
    # `ret, frame = vid.read()` is a line of code that reads the next video frame from the
    # `VideoCapture` object `vid` and assigns it to the variables `ret` and `frame`.
    ret, frame = vid.read()

    # `cv2.imshow("Web cam", frame)` is a function from the OpenCV library in Python that is used to
    # display an image or video frame in a window. In this code, it is used to display the video frame
    # captured from the webcam or video file in a window with the title "Web cam". The `frame`
    # variable contains the image data of the current video frame, and it is passed as an argument to
    # the `cv2.imshow()` function.
    cv2.imshow("Preview Window", frame)
    # The line `out.write(frame)` is writing the video frame captured from the webcam or video file to
    # the `VideoWriter` object `out`. This allows the frames to be saved and written to a video file.
    out.write(frame)
    # The line `if cv2.waitKey(25) == 32:` is checking if the key pressed is the spacebar key. If the
    # spacebar key is pressed, the `break` statement is executed, which exits the `while` loop and
    # stops capturing video frames. This allows the user to stop the video capture by pressing the
    # spacebar.
    if cv2.waitKey(25) == 32:
        break

# `vid.release()` is a function from the OpenCV library in Python that is used to release the
# `VideoCapture` object `vid` and free up any resources associated with it. This function is called at
# the end of the code to ensure that the video capture is properly closed and any resources used by it
# are released.
vid.release()
# The `out.release()` function is used to release the `VideoWriter` object `out` and free up any
# resources associated with it. This function is called at the end of the code to ensure that the
# video file being written is properly closed and saved.
out.release()

# `cv2.destroyAllWindows()` is a function from the OpenCV library in Python that is used to close all
# the windows created by the program. In this code, it is called at the end to close the window
# displaying the video feed from the webcam or video file.
cv2.destroyAllWindows()
