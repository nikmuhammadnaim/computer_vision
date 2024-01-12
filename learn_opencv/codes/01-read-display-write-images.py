import cv2

# Path to the image
img_path = "./images/luffy_card_raw.jpg"

# Read the image
img_luffy_ori = cv2.imread(img_path)
img_luffy_grayscaled = cv2.imread(img_path, 0)

# Display the image
cv2.imshow("Monkey D. Luffy", img_luffy_ori)
cv2.imshow("Monkey D. Luffy (Grayscaled)", img_luffy_grayscaled)

# Wait for a key press
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()

# Save the grayscale image
cv2.imwrite("images/luffy_card_grayscaled.jpg", img_luffy_grayscaled)
