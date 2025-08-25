# HillClimbRacing-Mediapipe Gesture Control 🎮

Play Hill Climb Racing using hand gestures! This project combines MediaPipe's hand tracking capabilities with OpenCV to create a fun and interactive way to control the game through your webcam.

## 🎯 Features

- Real-time hand tracking and gesture recognition
- Intuitive gesture controls:
  - **Left hand up** ⬆️: Accelerate (triggers `right` key)
  - **Right hand up** ⬆️: Brake (triggers `left` key)
- Visual feedback with hand landmarks and bounding boxes
- Low latency response for smooth gameplay

## 🛠️ Requirements

- Python 3.7 or higher
- Webcam
- Hill Climb Racing game
- Required Python packages:
  ```
  opencv-python >= 4.5.0
  mediapipe >= 0.8.9
  pydirectinput >= 1.0.4
  ```

## 📦 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/HillClimbRacing-Mediapipe.git
   cd HillClimbRacing-Mediapipe
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🎮 How to Play

1. Launch Hill Climb Racing
2. Open a terminal and run:
   ```sh
   python main.py
   ```
3. Position yourself in front of the webcam
4. Control the game with these gestures:
   - Raise left hand above shoulder → Accelerate
   - Raise right hand above shoulder → Brake
   - Both hands down → No action
5. Press `q` to exit the program

## 📁 Project Structure

```
HillClimbRacing-Mediapipe/
│
├── main.py          # Main game control script
├── requirements.txt # Project dependencies
└── README.md       # Project documentation
```

## 🔧 Configuration

The default webcam (index 0) is used. To use a different camera, modify the camera index in `main.py`:
```python
cap = cv2.VideoCapture(0)  # Change 0 to your desired camera index
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Troubleshooting

- **No camera detected**: Ensure your webcam is properly connected and not in use by other applications
- **Game not responding**: Make sure the game window is active and in focus
- **Lag in controls**: Try reducing the camera resolution in `main.py`

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for the hand tracking solution
- [OpenCV](https://opencv.org/) for image processing capabilities
- Hill Climb Racing game developers

---
Made with ❤️ by Abhinav