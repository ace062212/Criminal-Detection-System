# 🎯 Criminal Detection System
**2023 영상처리 프로젝트 - 복학 후 느낀 즐거움**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.7.0-green?style=for-the-badge&logo=opencv&logoColor=white)
![dlib](https://img.shields.io/badge/dlib-19.24.0-red?style=for-the-badge)

---

## 🌱 프로젝트 배경
2023년 복학 후 첫 전공 과목이었던 영상처리 수업에서 진행한 개인 프로젝트입니다. 
오랜만에 돌아온 학교 생활과 함께 만난 친구들, 그리고 새로운 기술에 대한 호기심이 만나 탄생한 작품입니다.

**개발 기간**: 2023년 5월 ~ 6월 (약 4주)  
**과목**: 영상처리 (전공선택 3학점)  
**성적**: A+  

---

## 🎉 왜 이 프로젝트가 특별했나?

복학 후 처음 들은 프로젝트 수업이었는데, 생각보다 **정말 재밌었다** 

- **실시간으로 얼굴이 인식되는 모습**을 처음 봤을 때의 신기함
- **OpenCV와 dlib**를 처음 다뤄보면서 느낀 컴퓨터 비전의 매력
- 같이 수업 듣던 친구들과 **"우와 이거 진짜 된다!"** 하면서 신나했던 기억
- 수배 포스터까지 자동으로 생성되는 걸 보고 **"내가 이런 걸 만들 수 있구나"** 싶었던 뿌듯함

단순히 과제를 위한 프로젝트가 아니라, 정말 **"재미있어서"** 밤새 코딩했던 기억이 선명.

---

## 🛠 핵심 기능

### 1. 실시간 얼굴 검출 & 자동 저장
```python
# 1초마다 자동으로 얼굴 캡처
if elapsed_time >= save_interval:
    face_img = frame[y_start:y_end, x_start:x_end]
    cv2.imwrite(face_filepath, resized_face_img)
```
- 웹캠을 통한 실시간 얼굴 검출
- 1초 간격으로 자동 캡처 및 저장
- 얼굴 영역 확대하여 더 정확한 이미지 추출

### 2. 똑똑한 중복 제거 시스템
두 가지 방식으로 중복을 검사해봤어요:

**방식 1: 랜드마크 기반 비교**
- 얼굴의 68개 특징점 추출
- 유클리디안 거리로 얼굴 비교

**방식 2: 임베딩 모델 활용 (더 정확!)**
```python
# dlib의 사전 훈련된 ResNet 모델 사용
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
embedding = np.array(facerec.compute_face_descriptor(image, shape))
```
- 임베딩 모델로 얼굴 특징 벡터 생성
- 임계값 0.4에서 최적 성능 확인

### 3. 자동 수배 포스터 생성
```python
# 검출된 얼굴을 흑백으로 변환하여 수배 포스터에 합성
face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
img_out[logo_y:logo_y+new_h, logo_x:logo_x+new_w] = cv2.cvtColor(face_gray, cv2.COLOR_GRAY2BGR)
```
- 중복 제거된 얼굴을 수배 포스터 템플릿에 자동 합성
- 흑백 효과로 더욱 사실적인 수배 포스터 생성

---

## 📊 프로젝트 결과

**최종 성과**:
- 실시간 처리 성능: 30fps 이상
- 얼굴 인식 정확도: 95% 이상
- 중복 제거 정확도: 임베딩 모델 사용 시 현저히 향상
- 최종 검출: 테스트에서 2명의 서로 다른 인물 정확히 식별

---

## 🧠 기술적 도전과 해결

### 중복 제거의 어려움
처음에는 단순히 랜드마크 좌표만 비교했는데, 정확도가 아쉬워서 임베딩 모델을 도입.
```python
# 임계값 실험 결과
# 0.1 ~ 100.0까지 약 40번의 테스트
# 최종 최적값: 0.4 (임베딩 모델 기준)
```

### 실시간 처리 최적화
- 이미지 크기 고정: 1200x1200
- 얼굴 영역 확장: 100픽셀씩 여유 공간 추가
- 처리 간격 조정: 1초마다 저장으로 성능 확보

---

## 📁 프로젝트 구조
```
Criminal-Detection-System/
├── src/
│   ├── main.py              # 메인 실행 파일
│   ├── face_detector.py     # 얼굴 검출 모듈
│   ├── face_processor.py    # 얼굴 처리 및 중복 검사
│   └── wanted_poster.py     # 수배 포스터 생성
├── notebooks/
│   └── 코드.ipynb          # 전체 개발 과정 노트북
├── data/
│   └── wanted/
│       └── template/       # 수배 포스터 템플릿
└── models/                 # 사전 훈련된 모델 (별도 다운로드 필요)
```

---

## 🚀 설치 및 실행

### 필수 모델 파일 다운로드
다음 파일들을 `models/` 폴더에 다운로드:
1. [shape_predictor_68_face_landmarks.dat](https://github.com/davisking/dlib-models)
2. [dlib_face_recognition_resnet_model_v1.dat](https://github.com/davisking/dlib-models)
3. [haarcascade_frontalface_alt2.xml](https://opencv.org/)

### 실행 방법
```bash
# 패키지 설치
pip install opencv-python dlib numpy matplotlib

# 실행
python src/main.py
```

---

## 💭 이 프로젝트를 통해 배운 것

### 기술적 성장
- **컴퓨터 비전 첫 입문**: OpenCV와 dlib 라이브러리 활용법
- **실시간 처리의 중요성**: 성능 최적화와 메모리 관리
- **머신러닝 모델 활용**: 사전 훈련된 모델을 실제 프로젝트에 적용

### 개발 경험
- **문제 해결 과정**: 단순한 랜드마크 비교에서 임베딩 모델로의 발전
- **실험과 검증**: 40번 이상의 임계값 테스트를 통한 최적화
- **결과물의 완성도**: 단순한 검출을 넘어 수배 포스터까지 생성

### 개인적 의미
복학 후 첫 전공 프로젝트였는데, **"이런 게 진짜 재밌구나!"** 하면서 데이터에 대한 열정을 다시 불러일으켜 준 프로젝트입니다. 
친구들과 함께 결과물을 보며 신기해했던 그 순간의 열정이 지금의 서의 나를 만들어준거같다.

---

## 🎯 향후 발전 방향

- **딥러닝 모델 직접 구현**: 사전 훈련된 모델이 아닌 직접 학습한 모델 적용
- **웹 애플리케이션 개발**: 더 많은 사람들이 쉽게 사용할 수 있도록
- **실시간 데이터베이스 연동**: 실제 수배자 정보와 연결

---

**Contact**: ace062212@gmail.com  
**GitHub**: [ace062212](https://github.com/ace062212)

*"복학 후 처음으로 정말 재미있게 만든 프로젝트"*
