import os
from pathlib import Path

# 프로젝트 루트 디렉토리 설정
ROOT_DIR = Path(__file__).parent.parent

# 모델 파일 경로
MODEL_DIR = ROOT_DIR / "models"
CASCADE_FILE = MODEL_DIR / "haarcascade_frontalface_alt2.xml"
LANDMARK_PREDICTOR_FILE = MODEL_DIR / "shape_predictor_68_face_landmarks.dat"
FACE_RECOGNITION_MODEL = MODEL_DIR / "dlib_face_recognition_resnet_model_v1.dat"

# 데이터 디렉토리 설정
DATA_DIR = ROOT_DIR / "data"
CAPTURED_DIR = DATA_DIR / "captured"
FACE_DIR = CAPTURED_DIR / "faces"
FACE_DIR_ALL = CAPTURED_DIR / "all"
WANTED_DIR = DATA_DIR / "wanted"
WANTED_TEMPLATE = WANTED_DIR / "template" / "wanted_template.jpg"
WANTED_OUTPUT = WANTED_DIR / "output"

# 이미지 설정
FIXED_WIDTH = 1200
FIXED_HEIGHT = 1200
EXTRA_WIDTH = 100
EXTRA_HEIGHT = 100

# 얼굴 인식 설정
FACE_COMPARE_THRESHOLD = 0.4
SAVE_INTERVAL = 1  # 초

# 디렉토리 생성
for dir_path in [FACE_DIR, FACE_DIR_ALL, WANTED_OUTPUT]:
    dir_path.mkdir(parents=True, exist_ok=True)