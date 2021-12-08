def blur(frame):
    image = cv2.imread(frame)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    text = "Not Blurry"
# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
    if fm < 100:
        text = "Blurry"
# show the image
    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    key = cv2.waitKey(0)