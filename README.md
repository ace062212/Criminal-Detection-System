# 🎯 Criminal Detection System
실시간 얼굴 인식 기술을 활용한 범죄자 식별 시스템

## 🎥 시연 영상 & 발표 자료
### 시연 영상
실제 시스템 작동 모습을 담은 시연 영상입니다. 주요 기능인 실시간 얼굴 인식, 수배 포스터 생성 등의 동작을 확인하실 수 있습니다.
- [시스템 시연 영상](demo/videos/시연영상.mov)

### 발표 자료
프로젝트의 상세 내용을 담은 발표 자료입니다.
- [프로젝트 발표 자료](docs/presentation/발표자료.pdf)


## 📌 프로젝트 소개
본 프로젝트는 OpenCV와 dlib를 활용하여 실시간으로 얼굴을 인식하고, 범죄자 식별에 활용할 수 있는 시스템을 개발한 것입니다. 실시간 영상에서 얼굴을 감지하고, 특징점을 추출하여 수배 시스템에 활용할 수 있도록 구현했습니다.

### 개발 기간
- 2023 .05 ~ 2023.06

## 🛠 기술 스택
### Languages & Libraries
- Python 3.8+
- OpenCV (영상 처리)
- dlib (얼굴 인식)
- NumPy (데이터 처리)

### Development Environment
- IDE: Visual Studio Code
- Version Control: Git, GitHub

## ⚙ 주요 기능
1. **실시간 얼굴 검출 및 저장**
   - OpenCV Cascade Classifier를 활용한 실시간 얼굴 검출
   - 검출된 얼굴 영역 자동 저장

2. **얼굴 특징점 추출**
   - dlib의 68-point face landmark detection 활용
   - 정확한 얼굴 특징점 추출 및 분석

3. **수배 포스터 자동 생성**
   - 검출된 얼굴 이미지 자동 변환
   - 수배 포스터 템플릿 적용

4. **중복 얼굴 검사**
   - 얼굴 특징 벡터 추출
   - 유클리디안 거리 기반 중복 검사

## 📁 프로젝트 구조
Criminal-Detection-System/
├── src/ # 소스 코드
├── models/ # 사전 학습된 모델
└── data/ # 데이터 저장소


## 🔍 구현 내용

### 1. 얼굴 검출 시스템
python
def detect_faces(self, frame):
"""OpenCV Cascade를 사용한 얼굴 검출"""
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
return self.cascade.detectMultiScale(gray, minSize=(30, 30))

- Haar Cascade Classifier를 활용한 실시간 얼굴 검출
- 정확도 향상을 위한 파라미터 최적화

### 2. 얼굴 특징점 추출
- dlib의 shape predictor를 활용한 68개 특징점 추출
- 추출된 특징점을 활용한 얼굴 분석

### 3. 수배 포스터 생성
- 자동화된 포스터 생성 시스템
- 이미지 처리를 통한 품질 개선

## 🎯 프로젝트 목표 및 성과
1. **실시간 처리 성능**
   - 초당 30프레임 이상의 처리 속도 달성
   - 지연 없는 얼굴 검출 및 저장

2. **정확도**
   - 다양한 각도에서의 얼굴 검출
   - 특징점 추출 정확도 95% 이상 달성

## 💡 개선 및 발전 계획
1. 딥러닝 모델 도입을 통한 정확도 향상
2. 실시간 범죄자 DB 연동 시스템 구축
3. 웹 인터페이스 개발을 통한 사용자 편의성 개선

## 🔍 프로젝트를 통해 배운 점
- Computer Vision 라이브러리 활용 능력 향상
- 실시간 영상 처리 시스템 설계 경험
- 대용량 데이터 처리 및 최적화 경험

## 📞 Contact
- Email: ace062212@gmail.com
- GitHub: [ace062212](https://github.com/ace062212)