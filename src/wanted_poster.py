import cv2
import numpy as np
from .config import *

class WantedPosterGenerator:
    def __init__(self):
        self.template = cv2.imread(str(WANTED_TEMPLATE))
        
    def generate_poster(self, face_image, save_path=None):
        """수배 포스터 생성"""
        if self.template is None:
            raise ValueError("수배 포스터 템플릿을 찾을 수 없습니다.")
            
        # 얼굴 이미지 크기 조정
        h, w, _ = face_image.shape
        scale_factor = 2.5
        new_h = int(h * scale_factor)
        new_w = int(w * scale_factor)
        face_resized = cv2.resize(face_image, (new_w, new_h))
        
        # 흑백 변환
        face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
        face_gray = cv2.cvtColor(face_gray, cv2.COLOR_GRAY2BGR)
        
        # 포스터에 얼굴 합성
        result = self.template.copy()
        center_y = result.shape[0] // 2 + 135
        center_x = result.shape[1] // 2
        y_offset = center_y - new_h // 2
        x_offset = center_x - new_w // 2
        
        result[y_offset:y_offset+new_h, 
               x_offset:x_offset+new_w] = face_gray
        
        # 저장
        if save_path:
            cv2.imwrite(str(save_path), result)
            
        return result