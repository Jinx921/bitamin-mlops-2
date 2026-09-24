"""BITAmin MLOps 2주차 통합 스냅샷.

1주차의 재현 가능한 실행 환경 위에 다음 협업 결과를 합친 상태다.
- 데이터 전처리
- Logistic Regression
- Random Forest
- 공통 평가 지표
"""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_PATH = Path(__file__).with_name("WA_FnUseC_TelcoCustomerChurn.csv")
RANDOM_STATE = 42


def load_data(path: Path) -> tuple[pd.DataFrame, pd.Series]:
    """CSV를 불러와 학습 입력과 타깃으로 분리한다."""
    df = pd.read_csv(path)

    # customerID는 식별자이므로 학습에서 제외한다.
    df = df.drop(columns=["customerID"])

    # 원본 데이터의 TotalCharges에는 공백 문자열이 포함되어 있다.
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    X = df.drop(columns=["Churn"])
    y = df["Churn"].map({"No": 0, "Yes": 1})
    return X, y


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """수치형과 범주형 컬럼에 서로 다른 전처리를 적용한다."""
    categorical_columns = X.select_dtypes(include=["object", "category"]).columns.tolist()

    # SeniorCitizen은 dtype상 수치형이지만 실제로는 이진 범주형 변수다.
    if "SeniorCitizen" in X.columns:
        categorical_columns.append("SeniorCitizen")

    numeric_columns = X.select_dtypes(exclude=["object", "category"]).columns.difference(
        categorical_columns
    )

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(drop="first", handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_columns),
            ("categorical", categorical_pipeline, categorical_columns),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_columns),
            ("categorical", categorical_pipeline, categorical_columns),
        ]
    )


def build_models() -> dict[str, object]:
    """2주차에 통합한 비교 모델을 반환한다."""
    return {
        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=RANDOM_STATE,
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            class_weight="balanced",
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
    }


def evaluate(y_true: pd.Series, y_pred, y_score) -> dict[str, float]:
    """불균형한 Churn 데이터에 필요한 공통 지표를 계산한다."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "roc_auc": roc_auc_score(y_true, y_score),
    }


def main() -> None:
    X, y = load_data(DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    results: dict[str, dict[str, float]] = {}

    for model_name, estimator in build_models().items():
        pipeline = Pipeline(
            steps=[
                ("preprocessor", build_preprocessor(X_train)),
                ("model", estimator),
            ]
        )
        pipeline.fit(X_train, y_train)

        y_pred = pipeline.predict(X_test)
        y_score = pipeline.predict_proba(X_test)[:, 1]
        results[model_name] = evaluate(y_test, y_pred, y_score)

    result_table = pd.DataFrame(results).T.sort_values("f1", ascending=False)
    print("=== Model comparison ===")
    print(result_table.round(4).to_string())
    print(f"\nBest model by F1: {result_table.index[0]}")


if __name__ == "__main__":
    main()
