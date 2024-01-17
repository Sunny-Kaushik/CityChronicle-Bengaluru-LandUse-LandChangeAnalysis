import rasterio
import numpy as np
import matplotlib.pyplot as plt

def image_difference(image1_path, image2_path, threshold=220):
    # Read the two images
    with rasterio.open(image1_path) as src1, rasterio.open(image2_path) as src2:
        image1 = src1.read(1)
        image2 = src2.read(1)
        transform = src1.transform  # Assuming both images have the same transform

    # Calculate the absolute difference between the two images
    diff = np.abs(image1 - image2)

    # Classify pixels based on the threshold
    changed_mask = (diff > threshold)

    # Create a new image with black for changed pixels and white for unchanged pixels
    output_image = np.where(changed_mask, 0, 255).astype(np.uint8)

    # Save or display the resulting image
    with rasterio.open('difference_result.tif', 'w', driver='GTiff', height=output_image.shape[0],
                       width=output_image.shape[1], count=1, dtype=np.uint8, crs=src1.crs, transform=transform) as dst:
        dst.write(output_image, 1)

    plt.imshow(output_image, cmap='gray')
    plt.show()

# Example usage
image1_path = 'lulc_bengaluru_2014.tif'
image2_path = 'lulc_bengaluru_2020.tif'
image_difference(image1_path, image2_path, threshold=220)
