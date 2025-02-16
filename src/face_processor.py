import cv2
import time
import numpy as np
from datetime import datetime
from .config import *

class FaceProcessor:
    def __init__(self, detector):
        """얼굴 처리 클래스 초기화"""
        self.detector = detector
        self.saved_face_features = []
        self.start_time = time.time()
        self.file_counter = 1
        self.file_counter_all = 1

    def process_frame(self, frame):
        """프레임 처리 및 얼굴 저장"""
        faces = self.detector.detect_faces(frame)
        current_time = time.time()
        
        if len(faces) > 0 and (current_time - self.start_time) >= SAVE_INTERVAL:
            self._save_detected_faces(frame, faces)
            self._draw_face_rectangles(frame, faces)
            self.start_time = current_time
            
        return frame

    def _save_detected_faces(self, frame, faces):
        """검출된 얼굴 저장"""
        for face in faces:
            x, y, w, h = face
            # 얼굴 영역 추출
            face_img = self._extract_face_region(frame, x, y, w, h)
            # 크기 조정
            resized_face = cv2.resize(face_img, (FIXED_WIDTH, FIXED_HEIGHT))
            
            # 얼굴 부분 저장
            self._save_face_image(resized_face, FACE_DIR)
            # 전체 화면 저장
            self._save_face_image(cv2.resize(frame, (FIXED_WIDTH, FIXED_HEIGHT)), FACE_DIR_ALL, suffix='all')

    def _extract_face_region(self, frame, x, y, w, h):
        """얼굴 영역 추출 (여유 공간 포함)"""
        x_start = max(0, x - EXTRA_WIDTH)
        y_start = max(0, y - EXTRA_HEIGHT)
        x_end = min(frame.shape[1], x + w + EXTRA_WIDTH)
        y_end = min(frame.shape[0], y + h + EXTRA_HEIGHT)
        return frame[y_start:y_end, x_start:x_end]

    def _save_face_image(self, image, save_dir, suffix=''):
        """이미지 저장"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        counter = self.file_counter if not suffix else self.file_counter_all
        filename = f"{counter}){timestamp}_{suffix}.jpg"
        cv2.imwrite(str(save_dir / filename), image)
        
        if suffix:
            self.file_counter_all += 1
        else:
            self.file_counter += 1

    def _draw_face_rectangles(self, frame, faces):
        """검출된 얼굴에 사각형 표시"""
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)