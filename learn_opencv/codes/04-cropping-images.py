import argparse
import os
import sys

import cv2
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Crop an image",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i",
        "--image",
        type=str,
        default="./images/luffy_card_raw.jpg",
        help="Path to the image file",
    )

    parser.add_argument(
        "-r",
        "--rows",
        type=int,
        default=3,
        help="Number of patches in the x direction",
    )

    parser.add_argument(
        "-c",
        "--cols",
        type=int,
        default=3,
        help="Number of patches in the y direction",
    )

    args = parser.parse_args()

    return args


def main(img_path: str, num_patches_x: int, num_patches_y: int):
    # Read the image
    img = cv2.imread(img_path)

    # Get the original image size (height, width)
    img_size = img.shape[:2]
    print(f"Image size: {img_size}")

    # Display the original image
    cv2.imshow("Original", img)

    # Crop the image (row [height], column[width])
    img_cropped = img[40:330, 220:460]

    # Display the cropped image
    cv2.imshow("Cropped", img_cropped)

    # Save the cropped image
    cv2.imwrite("./images/luffy_card_cropped.jpg", img_cropped)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

    # Create a copy of the image
    img_copy = img.copy()

    # Divide that into smaller patches
    divide_into_small_patches(img_copy, num_patches_x, num_patches_y)


def divide_into_small_patches(
    img: np.ndarray,
    num_patches_x: int = 3,
    num_patches_y: int = 3,
) -> list[np.ndarray]:
    """Divide an image into smaller patches.

    Parameters
    ----------
    img : np.ndarray
        The original image.
    num_patches_x : int
        The number of patches in the x direction.
    num_patches_y : int
        The number of patches in the y direction.

    Returns
    -------
    List[np.ndarray]
        A list of image patches.

    """
    # Calculate patch size
    patch_size_x = img.shape[0] // num_patches_x
    patch_size_y = img.shape[1] // num_patches_y

    # Divide the image into small patches
    img_patches = []
    for i in range(num_patches_x):
        for j in range(num_patches_y):
            start_x = patch_size_x * i
            end_x = patch_size_x * (i + 1)
            start_y = patch_size_y * j
            end_y = patch_size_y * (j + 1)

            img_patches.append(img[start_x:end_x, start_y:end_y])

    # Display the cropped image
    for i in range(num_patches_x * num_patches_y):
        window_name = f"Patch {i}"
        cv2.imshow(window_name, img_patches[i])
        # Re-arrenge the windows
        cv2.moveWindow(
            window_name,
            (i % num_patches_y) * img_patches[i].shape[1],
            (i // num_patches_y) * img_patches[i].shape[0]
        )

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

    return img_patches


if __name__ == "__main__":
    args = get_args()
    image_path = args.image
    num_patches_x = args.rows
    num_patches_y = args.cols

    # Check if the image path exists
    if not os.path.exists(image_path):
        print(f"ERROR: {image_path} does not exist")
        sys.exit(1)
    else:
        print(f"Reading image from {image_path}")

    main(image_path, num_patches_x, num_patches_y)
