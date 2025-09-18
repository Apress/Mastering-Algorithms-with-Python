import cv2 
import glob
import numpy as np
from PIL import Image 
from Listing_4_11_seam_carving_calculate_gradient import calculate_energy, calculate_gradient
from Listing_4_12_seam_carving_calculate_cumulative_energy import calculate_cumulative_energy
from Listing_4_13_find_single_seam import find_single_seam_from_cumu_energy

def seam_carving(color_image, gray_scale_image, num_seams = 10):
    I = gray_scale_image
    for i in range(num_seams):
        R = len(I)
        C = len(I[0])
        Ix, Iy = calculate_gradient(I.tolist())
        E = calculate_energy(Ix, Iy)
        cumu_E = calculate_cumulative_energy(E) 
        seam_pixels_indexes = find_single_seam_from_cumu_energy(cumu_E)
        # draw seams as red
        for r, c in seam_pixels_indexes:
            color_image[:, :, 0][r,c] = 0  # this is blue channel
            color_image[:, :, 1][r,c] = 0    # this is green channel
            color_image[:, :, 2][r,c] = 255    # this is red channel
        cv2.imshow("current_seam", color_image)
        cv2.imwrite(f"tower_images/seam_#{i + 1}.jpg", color_image)
        # remove seam
        mask = np.ones((R, C), dtype = bool)
        for r, c in seam_pixels_indexes:
            mask[r][c] = False 

        blue_channel = color_image[:, :, 0][mask].reshape(R, C-1)
        green_channel = color_image[:, :, 1][mask].reshape(R, C-1)
        red_channel = color_image[:, :, 2][mask].reshape(R, C-1)
        gray_channel = I[mask].reshape(R, C-1)
        color_image = np.dstack((blue_channel,green_channel,red_channel))
        I = gray_channel
    cv2.imwrite(f"final_image_after_seam_carving.jpg", color_image)

def create_a_gif(fp_in = "tower_images/*.jpg", fp_out = "seam_carving_in_action.gif"):
    imgs = (Image.open(f) for f in sorted(glob.glob(fp_in), 
                                          key = lambda image_name: int(image_name.split(".")[0].split("#")[1])))
    img = next(imgs)
    img.save(fp = fp_out, 
             format = "GIF",
             append_images = imgs,
             save_all = True, 
             duration=10,
             loop=0)

if __name__ == "__main__":
    gray_scale_image = cv2.imread('Broadway_Tower.jpg', cv2.IMREAD_GRAYSCALE)
    color_image = cv2.imread('Broadway_Tower.jpg', cv2.IMREAD_COLOR)
    seam_carving(color_image, gray_scale_image, num_seams = 500)
    create_a_gif()