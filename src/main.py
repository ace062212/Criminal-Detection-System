import cv2
import time
from .face_detector import FaceDetector
from .face_processor import FaceProcessor
from .config import *

def main():
    # 초기화
    detector = FaceDetector()
    processor = FaceProcessor(detector)
    
    # 카메라 캡처 시작
    cap = cv2.VideoCapture(0)
    
    print("얼굴 인식 시스템이 시작되었습니다.")
    print("종료하려면 'q'를 누르세요.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("카메라를 찾을 수 없습니다.")
                break

            # 프레임 처리
            processed_frame = processor.process_frame(frame)
            
            # 화면 출력
            cv2.imshow("Face Detection", processed_frame)
            
            # 'q' 키로 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("프로그램을 종료합니다.")
                break

    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")
        
    finally:
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

if __name__ == "__main__":
    main()