import cv2
import pandas as pd

# Define the paths and headers for the CSV file and image
csv_path = "colors.csv"
img_path = "images/pic3.jpeg"
headers = ['color', 'color_name', 'hexa', 'R', 'G', 'B']

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_path)
df.columns = headers

# Load the image using OpenCV
img = cv2.imread(img_path)
img=cv2.resize(img,(800, 600))

# Initialize variables for mouse click events
clicked = False
r = g = b = x_pos = y_pos = 0

# function to get nearest matching color name from color.csv dataset ,when clicked on the image by passing rgb values of the image

def get_color_name(R,G,B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R-int(df.loc[i,'R'])) + abs(R-int(df.loc[i,'G'])) + abs(B-int(df.loc[i,'B']))
        if d <= minimum:
            minimum =d
            c_name = df.loc[i,'color_name']

    return c_name


# Reading mouse pints on the image
def mousePoints(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global clicked, x_pos, y_pos, r, g, b
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Create an OpenCV window and set the mouse callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', mousePoints)

# Main loop for displaying the image and processing mouse clicks
while True:
    cv2.imshow('image', img)
    if clicked:
        cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) +' , '+ f" RGB: ({r}, {g}, {b})"
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if r+g+b >= 550:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # Exit the loop and close the window when 'q' is pressed
    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        break

# close all the opencv  windows
cv2.destroyAllWindows()
