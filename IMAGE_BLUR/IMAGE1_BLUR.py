import cv2

# Defining Image Blur Effect Functions
def blur_img(img, factor = 20):
    kW = int(img.shape[1] / factor)
    kH = int(img.shape[0] / factor)

    # Ensure the shape of the kernel is odd
    if kW % 2 == 0: kW = kW - 1
    if kH % 2 == 0: kH = kH - 1

    blurred_img = cv2.GaussianBlur(img, (kW, kH), 0)
    return blurred_img

# Loading Images
img = cv2.imread("img1.png")
blurred_img = blur_img(img, factor = 10)
background_blur_img = blur_img(img, factor = 10)

# Find face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(img, 1.3, 5)

# Blur Image and Face Combination
for (x, y, w, h) in faces:
    detected_face = img[int(y):int(y+h), int(x):int(x+w)]
    background_blur_img[y:y+h, x:x+w] = detected_face

cv2.imshow('img', img)
cv2.imshow('blur_img', blurred_img)
cv2.imshow('background_blur_img', background_blur_img)
# Output only one if multiple faces are present
cv2.imshow('face', detected_face)

cv2.waitKey(0)
cv2.destroyAllWindows()
