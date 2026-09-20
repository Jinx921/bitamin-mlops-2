import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# 1. 데이터 로드
df = pd.read_csv("WA_FnUseC_TelcoCustomerChurn.csv")

# 2. 학습에 사용하지 않을 컬럼 제거
df = df.drop(columns=["customerID"])

# 3. TotalCharges 숫자형 변환
# 변환할 수 없는 공백 값은 NaN으로 처리
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# 4. 입력(X)과 타깃(y) 분리
X = df.drop(columns=["Churn"])
y = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# 수치형 / 범주형 컬럼 구분
numeric_cols = X.select_dtypes(
    include=["int64", "float64"]
).columns

categorical_cols = X.select_dtypes(
    include=["object"]
).columns

# 수치형 전처리
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

# 범주형 전처리
categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore")),
])

# 전체 전처리 Pipeline
preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_cols),
    ("cat", categorical_transformer, categorical_cols),
])

# 5. 학습 / 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 6. 전처리
# train 데이터로만 전처리기를 학습
X_train_processed = preprocessor.fit_transform(X_train)

# test 데이터에는 train에서 학습한 전처리 적용
X_test_processed = preprocessor.transform(X_test)

# 7. Logistic Regression 학습
lr_model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced",
    random_state=42
)

lr_model.fit(
    X_train_processed,
    y_train
)

lr_pred = lr_model.predict(
    X_test_processed
)

# 8. Random Forest 학습
rf_model = RandomForestClassifier(
    n_estimators=200,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

rf_model.fit(
    X_train_processed,
    y_train
)

rf_pred = rf_model.predict(
    X_test_processed
)

# 9. 평가
lr_acc = accuracy_score(
    y_test,
    lr_pred
)

lr_f1 = f1_score(
    y_test,
    lr_pred
)

rf_acc = accuracy_score(
    y_test,
    rf_pred
)

rf_f1 = f1_score(
    y_test,
    rf_pred
)

# 10. 결과 출력
print("=== Logistic Regression ===")
print(f"Accuracy: {lr_acc:.4f}")
print(f"F1 Score: {lr_f1:.4f}")

print()

print("=== Random Forest ===")
print(f"Accuracy: {rf_acc:.4f}")
print(f"F1 Score: {rf_f1:.4f}")