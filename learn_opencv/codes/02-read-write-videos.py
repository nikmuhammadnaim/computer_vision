import argparse
import os
import sys

import cv2


def get_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Read and display a video file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-v",
        "--video",
        type=str,
        default="./videos/luffy_gear5.mp4",
        help="Path to the video file",
    )

    args = parser.parse_args()

    return args


def main(vid_path: str):
    # Get the filename
    filename = os.path.basename(vid_path)

    # Create a video capture object to read the video
    vid_capture = cv2.VideoCapture(vid_path)

    if vid_capture.isOpened() is False:
        print(f"Error: the video file {filename} cannot be opened!")
    else:
        # Get the frame rate information
        fps = vid_capture.get(cv2.CAP_PROP_FPS)
        print(f"FPS: {fps}")

        # Get the frame count
        frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        print(f"Frame count: {frame_count}")

        # Calculate the duration of the video in seconds
        duration_in_seconds = frame_count / fps
        print(f"Duration: {duration_in_seconds} seconds")

        # Get the frame width, height, and size
        frame_width = int(vid_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(vid_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_size = (frame_width, frame_height)
        print(f"Frame size: {frame_size}")

        # Create a new video with different format
        new_filename = vid_path.replace(".mp4", ".avi")

        # Initialize the video writer object
        vid_writer = cv2.VideoWriter(
            new_filename,
            cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
            fps,
            (980, 640),
            isColor=True,  # Add this argument to specify color video
        )

    while vid_capture.isOpened():
        # Read the video frame-by-frame
        ret, frame = vid_capture.read()

        if ret is True:
            # Resize the frame
            resized_frame = cv2.resize(frame, (980, 640))

            # Write the frame to the output files
            vid_writer.write(resized_frame)

            # Display the frame at the resized frame
            cv2.imshow(filename, resized_frame)

            # Wait for a key press
            if cv2.waitKey(int(1000/fps)) & 0xFF == ord("q"):
                break
        else:
            break

    # Release the video capture object
    vid_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    args = get_args()
    vid_path = args.video

    # Check if the file in the given path exist
    if os.path.exists(vid_path) is False:
        print(f"Error: the video file {vid_path} does not exist!")
        sys.exit(1)

    main(vid_path)
