import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

class custom_apps(object):
    def __init__(self):
        print('hi')
    def resize_im(self, image, size, interp = 'NN'):
        resized_image = self.make_empty_color(size[0], size[1])
        x_des, y_des = size[0], size[1]
        x_initial, y_initial, ch = image.shape
        print("initial size:" , (x_initial, y_initial))

        scale_f = [x_des/x_initial, y_des/y_initial]
        print("scale factor", scale_f)


        if interp == 'NN':
            Int_row_indices = np.ceil((np.array(range(y_des))+ 1)/scale_f[1]).astype(int)
            print(Int_row_indices)
            Int_col_indices = np.ceil((np.array(range(x_des))+ 1)/scale_f[0]).astype(int)


            print('length of col,', len(Int_col_indices))
            print('length of row', len(Int_row_indices))
            print(resized_image.shape)

            resized_image = image[Int_col_indices - 1, :, :]
            resized_image = resized_image[:, Int_row_indices - 1, :]

            plt.title('original')
            plt.imshow(image)
            plt.show()

            plt.title("scaled")
            plt.imshow(resized_image)
            plt.show()
            print(resized_image.shape)
            print('upsample with nearest neighbors')

    def make_empty(self, image):
        return np.zeros_like(image)
    def make_empty_color(self, height, width):
        return np.zeros((height, width, 3), np.uint8)


image = cv2.imread("Images/Mario.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(image.shape)
#plt.imshow(image)
#plt.show()

CV_lib = custom_apps()
CV_lib.resize_im(image, [640,800])
