# Finger Sketch

A simple Python application that allows users to draw on the screen using their finger (or mouse). This project leverages computer vision techniques to track finger movements and convert them into digital sketches in real-time.

## Features

- Draw on the screen using your finger or a pointing device.
- Real-time tracking and sketching.
- Adjustable brush size and color (if implemented).
- Clear or save the sketch (if implemented).

## Demo

Include a GIF or screenshot showing the application in action:

![Finger Sketch Demo](path_to_demo_image.gif)

## Requirements

- Python 3.8+
- OpenCV
- NumPy (optional, depending on your implementation)

Install dependencies using:

```bash
pip install opencv-python numpy
````

## Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/finger-sketch.git
cd finger-sketch
```

2. Run the application:

```bash
python finger_sketch.py
```

3. Use your finger in front of the webcam to draw on the screen.

   * Press `c` to clear the canvas.
   * Press `q` to quit the application.

*(Adjust keys based on your implementation.)*

## How It Works

1. The webcam captures live video feed.
2. The application detects the finger tip using computer vision techniques.
3. The finger movement is tracked and drawn on a virtual canvas in real-time.

## Potential Improvements

* Add color and brush size selection.
* Save sketches automatically.
* Multi-finger gesture support.
* Mobile application integration.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

* **Ajay Sivakumar** – [GitHub](https://github.com/yourusername)

```

