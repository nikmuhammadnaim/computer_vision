import argparse
import os
import sys

import cv2


def get_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Resize an image",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i",
        "--image",
        type=str,
        default="./images/luffy_card_raw.jpg",
        help="Path to the image file",
    )

    args = parser.parse_args()

    return args


def main(img_path: str):
    """Main function."""
    # Read the image
    img = cv2.imread(img_path)

    # Get the original image size (height, width)
    img_size = img.shape[:2]
    print(f"Image size: {img_size}")

    # Display the original image
    cv2.imshow("Original", img)

    # Downsize the image
    img_downsized = cv2.resize(
        img,
        None,
        fx=0.5,
        fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    # Display the downsized image
    cv2.imshow("Downsized", img_downsized)

    # Upsize the image
    img_upsized = cv2.resize(
        img,
        None,
        fx=1.5,
        fy=1.5,
        interpolation=cv2.INTER_CUBIC
    )

    # Display the upsized image
    cv2.imshow("Upsized", img_upsized)

    # Wait for a key press
    cv2.waitKey(0)

    # Destroy all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Get command-line arguments
    args = get_args()
    img_path = args.image

    # Check if the file in the given path exist
    if os.path.exists(img_path) is False:
        print(f"Error: the image file {img_path} does not exist!")
        sys.exit(1)
    else:
        print(f"Reading image from {img_path}...")

    # Call the main function
    main(img_path)
