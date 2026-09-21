# 2주차 완료 상태

Git/GitHub의 branch, commit, Pull Request, review, merge 흐름을 거쳐 여러 사람의 변경을 하나의 코드베이스로 통합한 결과다.

## 통합된 역할

| 역할 | 최종 코드에 반영된 내용 |
|---|---|
| 데이터 전처리 담당 | 결측치 처리, 수치형/범주형 전처리 pipeline |
| Logistic Regression 담당 | 불균형을 고려한 Logistic Regression |
| Random Forest 담당 | 비교용 Random Forest 모델 |
| 평가 담당 | Accuracy, Precision, Recall, F1, ROC-AUC 출력 |

## 정상 실행 확인

```bash
python app.py
```

정상적으로 실행되면 두 모델의 평가표와 F1 기준 best model이 출력된다.

```text
=== Model comparison ===
                     accuracy  precision  recall      f1  roc_auc
Logistic Regression       ...        ...     ...     ...      ...
Random Forest             ...        ...     ...     ...      ...

Best model by F1: ...
```

Docker에서도 같은 명령이 실행된다.

```bash
docker build -t bitamin-mlops-week2 .
docker run --rm bitamin-mlops-week2
```

## Snapshot에서 확인할 수 없는 것

branch 생성, review comment, Merge Conflict 해결은 Git 이력과 Pull Request에서 발생하는 과정이다. 이 snapshot은 모든 충돌이 해결되어 main에 통합된 **최종 코드 상태**만 제공한다.

각 조는 자신의 repository에서 직접 branch와 Pull Request를 만들고, 실행 화면 및 충돌 해결 과정을 `week2/README.md`에 기록해야 한다. 이 문서를 조별 실습 증거로 그대로 제출하면 안 된다.

## Week2 Result

Git / GitHub 기반 협업 실습을 완료했습니다.