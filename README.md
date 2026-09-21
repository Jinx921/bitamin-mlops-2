# BITAmin 17기 MLOps 프로젝트 - 2조

> **Telco Customer Churn 데이터를 활용한 고객 이탈 방지 서비스 구축**

BITAMIN 17기 MLOps 세션 **2조 공용 Repository**

하나의 고객 이탈 예측 프로젝트를 기반으로  
**개발환경 구축 → 협업 → 실험 관리 → 모델 서빙 → CI/CD**까지  
5주 동안 MLOps의 전체 흐름 경험

---

## 📚 Curriculum

| Week | Topic | Goal |
|---|---|---|
| 1 | 재현 가능한 ML 개발환경 | Conda / Docker 기반 실행환경 구축 |
| 2 | Git / GitHub 기반 협업 | Branch / PR 기반 협업 |
| 3 | WandB 실험 관리 | 실험 기록 및 Best Model 선정 |
| 4 | FastAPI 모델 서빙 | 예측 API 구축 |
| 5 | Docker + GitHub Actions CI/CD | 테스트 및 배포 자동화 |

5주 동안 동일한 조별 Repository를 계속 사용하며 이전 주차 결과물 위에 다음 실습을 이어감

---

## 📁 Repository Structure

```text
bitamin-mlops-2/
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
├── WA_FnUseC_TelcoCustomerChurn.csv
│
├── week1/
│   └── README.md
└── week2/
    └── README.md
```

각 주차의 세부 실습 과정과 체크포인트 결과는  
해당 `weekN/README.md`에 기록

---

## ✅ Week 1 — 재현 가능한 ML 개발환경

- Conda 가상환경 구축
- Python 3.10 환경 구성
- `requirements.txt` 기반 패키지 설치
- Baseline Logistic Regression 실행
- Docker Image Build
- Docker Container 실행

---

## ✅ Week 2 — Git / GitHub 기반 협업

각 조원이 별도의 Branch에서 기능을 구현한 뒤  
Pull Request와 Code Review를 통해 `main`에 통합

| Branch | 작업 |
|---|---|
| `feature/preprocessing` | 데이터 전처리 개선 |
| `feature/logistic-regression` | Logistic Regression 개선 |
| `feature/random-forest` | Random Forest 추가 |
| `feature/evaluation-metrics` | 평가 Metric 추가 |

## 🤖 Current Model

현재 `app.py`에는 다음 내용이 통합되어 있음

- `ColumnTransformer` 기반 전처리
- 결측치 처리
- One-Hot Encoding / Scaling
- Logistic Regression
- Random Forest
- Accuracy / F1 Score 평가

---

## ▶️ Run

### Conda 환경 활성화

```bash
conda activate mlops-week1
```

### 패키지 설치

```bash
pip install -r requirements.txt
```

### 모델 실행

```bash
python app.py
```

실행 결과 예시:

```text
=== Logistic Regression ===
Accuracy: 0.7381
F1 Score: 0.6136

=== Random Forest ===
Accuracy: 0.7850
F1 Score: 0.5444
```

---

## 🌿 Git Workflow

작업 시작 전 최신 `main`을 반영

```bash
git switch main
git pull origin main
```

새로운 Branch에서 작업

```bash
git switch -c <branch-name>
```

작업 후 Commit & Push

```bash
git add .
git commit -m "<commit-message>"
git push -u origin <branch-name>
```

이후 GitHub에서

```text
Pull Request → Code Review → Merge
```

순서로 `main`에 반영

---
branch protection test 리드미 파일