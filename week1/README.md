# 1주차 완료 상태

재현 가능한 ML 개발환경을 구축하고 baseline 고객 이탈 예측 코드를 실행한다.

## 포함된 결과

- Python 3.10 실행 환경
- 패키지 버전이 명시된 `requirements.txt`
- Telco Customer Churn 데이터셋
- baseline 학습 코드
- Docker 이미지 빌드 및 컨테이너 실행 환경

## 실행 명령어

```bash
pip install -r requirements.txt
python app.py

docker build -t bitamin-mlops-week2 .
docker run --rm bitamin-mlops-week2
```

원본 1주차 스냅샷: <https://github.com/chowonmoon/bitamin-mlops-1-snapshot>
