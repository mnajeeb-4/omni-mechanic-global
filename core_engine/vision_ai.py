"""
Computer Vision module using YOLOv8 & OpenCV.
Draws Red/Yellow AR bounding boxes on live frames.
"""
import cv2
import numpy as np
from ultralytics import YOLO
import streamlit as st

@st.cache_resource
def load_yolo_model():
    try:
        return YOLO('yolov8n.pt')
    except Exception:
        return None  # Fallback to mock detection

class VisionAI:
    def __init__(self):
        self.model = load_yolo_model()
        self.colors = {
            "CRITICAL": (0, 0, 255),    # BGR Red
            "WARNING": (0, 255, 255),   # BGR Yellow
            "HEALTHY": (0, 255, 0)      # BGR Green
        }

    def _draw_ar_box(self, frame, x1, y1, x2, y2, label, severity):
        color = self.colors.get(severity, (255, 255, 255))
        # Draw glowing border
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
        # Draw text label with Claymorphism-style dark background
        text = f"{label}: {severity}"
        (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        cv2.rectangle(frame, (x1, y1 - th - 10), (x1 + tw + 12, y1), (20, 20, 30), -1)
        cv2.rectangle(frame, (x1, y1 - th - 10), (x1 + tw + 12, y1), color, 1)
        cv2.putText(frame, text, (x1 + 6, y1 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        return frame

    def process_frame(self, frame: np.ndarray) -> tuple[np.ndarray, list]:
        """Process a BGR frame. Returns annotated frame and detection results."""
        detections = []
        if self.model is None:
            # Mock detection for demo/fallback
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > 1000:
                    x, y, w, h = cv2.boundingRect(cnt)
                    severity = "CRITICAL" if area > 5000 else "WARNING"
                    self._draw_ar_box(frame, x, y, x+w, y+h, "Anomaly", severity)
                    detections.append({"label": "Anomaly", "severity": severity})
        else:
            # Real YOLO inference
            results = self.model(frame)[0]
            for box in results.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = self.model.names[cls]
                severity = "CRITICAL" if conf > 0.7 else "WARNING"
                self._draw_ar_box(frame, x1, y1, x2, y2, label, severity)
                detections.append({"label": label, "severity": severity, "confidence": conf})
        
        return frame, detections
