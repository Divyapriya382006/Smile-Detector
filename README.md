
```markdown
# Smile Detector

A Python project to detect smiles in faces using a pre-trained Haar Cascade smile detection model.  
Optimized for real-time detection with grayscale conversion.

## Features
- Detect smiles in real-time or from images
- Convert BGR images to grayscale for better performance
- Draw rectangles around detected smiles with optional text

## How It Works
1. Convert input image/video frame to grayscale
2. Load Haar Cascade smile detection model
3. Detect smiles in the grayscale image
4. Draw rectangles around detected smiles and display optional text

## Technologies Used
- Python
- OpenCV (`cv2`)

## Usage
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install opencv-python
