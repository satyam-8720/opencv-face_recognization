# Face Detection and Recognition System

This repository provides a complete pipeline for face detection and face recognition using OpenCV. It includes scripts to:
- Detect faces in an image.
- Detect faces in real-time using webcam.
- Train a recognizer on labeled face images.
- Recognize known faces from new images using the trained model.

## 📁 Project Structure

```
.
├── face_detection.py         # Detects faces from a static image
├── face_detectionvid.py      # Detects faces in real-time from webcam
├── face_train1.py            # Trains the model with labeled images
├── face_recognization1.py    # Recognizes faces using trained model
├── haar_cascade.xml          # Haar Cascade classifier for face detection
├── face_trained.yml          # Trained LBPH model (generated after training)
├── features.npy              # Saved face features (generated after training)
├── labels.npy                # Saved labels corresponding to face data
```

## 📌 Requirements

Make sure you have the following installed:

- Python 3.6+
- OpenCV (with `opencv-contrib-python` for face recognition module)
- NumPy

Install dependencies via pip:
```bash
pip install opencv-python opencv-contrib-python numpy
```

## 📸 Dataset Preparation

Before training, organize the dataset like this:
```
Faces/
└── train/
    ├── Ben Afflek/
    ├── Elton John/
    ├── Jerry Seinfield/
    ├── Madonna/
    └── Mindy Kaling/
└── val/
    └── (same structure as train for validation/testing)
```

Update the `dir` path in `face_train1.py` and `face_recognization1.py` according to your system.

## 🚀 How to Use

1. **Train the Recognizer**
   ```bash
   python face_train1.py
   ```

2. **Recognize a Face**
   ```bash
   python face_recognization1.py
   ```

3. **Face Detection in an Image**
   ```bash
   python face_detection.py
   ```

4. **Real-Time Face Detection via Webcam**
   ```bash
   python face_detectionvid.py
   ```
   Press **`d`** to exit webcam view.

## 🧠 Model Used

- **Face Detection**: Haar Cascade Classifier (`haar_cascade.xml`)
- **Face Recognition**: Local Binary Patterns Histograms (LBPH)

## 📌 Notes

- Accuracy depends on image quality, lighting, and face visibility.
- `haar_cascade.xml` must be present in the same directory.
- Ensure consistent face alignment and frontal images for better training performance.

## 📄 License

This project is for educational purposes.

## 🙋‍♂️ Author

**Satyam Chauhan**  
Feel free to reach out or contribute improvements to this project!