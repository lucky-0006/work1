# The code snippet is importing the necessary modules `os` and `cv2` for file and image processing. It
# then sets the `path` variable to the directory path where theimagesList are located. The `images` list
# is initialized to store the file paths of theimagesList .
# The code snippet is importing the necessary modules `os` and `cv2` for file and image processing. It
# then sets the `path` variable to the directory path where theimagesList are located. The `images` list
# is initialized to store the file paths of theimagesList .
import os 
import cv2


path = "C:/Users/HP/Desktop/python/C105/Images"

imagesList = []


# The code snippet is iterating over the files in the directory specified by the `path` variable using
# the `os.listdir()` function. For each file, it extracts the name and extension using the
# `os.path.splitext()` function. If the extension is one of ['.gif', '.png', '.jpg', '.jpeg',
# '.jfif'], it constructs the full file path by concatenating the `path` and `file` variables and
# appends it to the `images` list.
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print()
        print("FILE NAME:-  ")
        print(file_name)       
        imagesList.append(file_name)
        
#print(len(images))
# `count = len(images)` is calculating the number ofimagesList in the `images` list and assigning it to
# the variable `count`.
count = len(imagesList)
print("number of images in the list:-  ",count)
print()



# The code `frame = cv2.imread(imagesList[0])` reads the first image in the `imagesList` list using the
# `cv2.imread()` function and assigns it to the variable `frame`.
frame = cv2.imread(imagesList[0])
height, width, channels = frame.shape
size = (width,height)
print("SIZE, that is width and height of a video frame:-  ",size)



#For SUNSET
sunsetVideoObject = cv2.VideoWriter('sunset.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(0, count-1):
    frame = cv2.imread(imagesList[i])
    sunsetVideoObject.write(frame)

#For SUNRISE
sunriseVideoObject = cv2.VideoWriter('sunrise.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

# The code snippet `for i in range(count-1,0,-1):` is a loop that iterates over a range of numbers in
# reverse order.
for i in range(count-1, 0, -1):
    frame = cv2.imread(imagesList[i])
    sunriseVideoObject.write(frame)
    
# `out.release()` is a method in OpenCV that releases the video writer object and frees up any
# resources associated with it. It is necessary to call this method after writing all the frames to
# the video file.
sunsetVideoObject.release() # releasing the video generated
print("Sunset video Done")
sunriseVideoObject.release()
print("Sunrise video Done")

