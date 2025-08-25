# HillClimbRacing-Mediapipe Gesture Control

This project uses [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/) to control the Hill Climb Racing game using hand gestures detected from your webcam.

## Features

- Detects left and right hands using MediaPipe.
- Draws bounding boxes and labels for detected hands.
- Uses hand gestures (middle finger tip above wrist) to simulate keyboard presses:
  - **Left hand up:** Presses the `right` key.
  - **Right hand up:** Presses the `left` key.
- Real-time webcam feed with gesture visualization.

## Requirements

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [PyDirectInput](https://pypi.org/project/pydirectinput/)

Install dependencies with:

```sh
pip install opencv-python mediapipe pydirectinput
```

## Usage

1. Make sure Hill Climb Racing is running and focused.
2. Run the script:

    ```sh
    python main.py
    ```

3. Use your webcam to show your hands:
    - Raise your **left hand** to accelerate (`right` key).
    - Raise your **right hand** to brake (`left` key).
4. Press `q` to quit.

## File Structure

- [`main.py`](main.py): Main script for gesture detection and game control.

## Notes

- The script uses your webcam (device 0).
- Make sure the game window is active to receive keyboard inputs.

## License

MIT