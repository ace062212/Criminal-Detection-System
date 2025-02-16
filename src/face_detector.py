import cv2
import dlib
import numpy as np
from .config import *

class FaceDetector:
    def __init__(self):
        """얼굴 검출 및 인식 관련 초기화"""
        self.cascade = cv2.CascadeClassifier(str(CASCADE_FILE))
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(str(LANDMARK_PREDICTOR_FILE))
        self.facerec = dlib.face_recognition_model_v1(str(FACE_RECOGNITION_MODEL))

    def detect_faces(self, frame):
        """OpenCV Cascade를 사용한 얼굴 검출"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return self.cascade.detectMultiScale(gray, minSize=(30, 30))

    def extract_face_embedding(self, image):
        """dlib을 사용한 얼굴 특징 추출"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_rects = self.detector(gray, 1)
        
        if len(face_rects) == 1:
            shape = self.predictor(image, face_rects[0])
            return np.array(self.facerec.compute_face_descriptor(image, shape))
        return None

    def get_landmarks(self, image, face):
        """얼굴 랜드마크 추출"""
        shape = self.predictor(image, face)
        return np.array([[p.x, p.y] for p in shape.parts()])