import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('test.jpg')  # 'test.jpg'는 이미지 파일 경로

# 이미지가 제대로 로드되었는지 확인
if image is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 1. 그레이스케일 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)

# 2. 이미지 블러 처리
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred Image", blurred_image)

# 3. 엣지 검출 (Canny Edge Detection)
edges = cv2.Canny(gray_image, 100, 200)
cv2.imshow("Edge Detection", edges)

# 4. 이미지 저장
cv2.imwrite('output.jpg', edges)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
