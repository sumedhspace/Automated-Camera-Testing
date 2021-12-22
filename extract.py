import cv2
import matplotlib.pyplot as plt
path ="edge.png"
src = cv2.imread(path)

image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )
#blur = cv2.GaussianBlur(image,(5,5),0)
edges = cv2.Canny(image,100,200)
plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()