# Week 2 체크포인트

Git / GitHub 기반 협업 실습의 체크포인트를 정리합니다.

- **필수 체크포인트**: 통과 여부 판정에 포함
- **심화 체크포인트**: 통과 여부 판정에 미포함, 시간이 남는 조에 한하여 수행
- 필수 체크포인트의 예상 소요 시간 합계는 **35분**입니다.

---

## 1. 필수 체크포인트

| 번호 | 체크포인트 | 통과 확인 화면 | 예상 시간 |
|---|---|---|---:|
| 1 | 조별 Repository 개설 및 1주차 결과물 Push | GitHub에 `week1` 폴더 표시 | 7분 |
| 2 | 조원 전원이 각자 Branch 생성 후 작업 | Branch 목록에 4개 이상 표시 | 5분 |
| 3 | 조원 전원이 PR 생성 및 최소 1건 Review Comment 작성 | PR 목록 및 Review Comment 화면 | 10분 |
| 4 | 모든 PR Merge 완료 | Merge 완료된 PR 화면 | 5분 |
| 5 | Merge Conflict 1건 이상 발생 및 해결 | Conflict 화면과 해결 후 Commit | 8분 |

**필수 체크포인트 예상 시간 합계: 35분**

---

## 2. 심화 체크포인트

| 번호 | 체크포인트 | 통과 확인 화면 | 권장 예상 시간 |
|---|---|---|---:|
| 1 | Issue 생성 및 Commit Convention 적용 | Issue Timeline에 관련 Commit 표시 + Convention이 적용된 Commit History | 5분 |
| 2 | PR Template 작성 및 적용 | `.github/pull_request_template.md` 생성 + 새 PR에서 Template 자동 표시 | 3분 |
| 3 | Branch Protection 설정 및 동작 확인 | `main` Ruleset 활성화 + Review 전 Merge 제한 화면 | 5분 |

**심화 체크포인트 권장 예상 시간 합계: 13분**

> 심화 체크포인트는 필수 통과 판정에 포함되지 않습니다.  
> 필수 체크포인트를 모두 완료한 뒤 시간이 남는 조가 선택적으로 진행합니다.

---

## 3. 체크포인트별 확인 사항

### 필수 1. 조별 Repository 개설 및 1주차 결과물 Push

- Repository 이름: `bitamin-mlops-{조번호}`
- Public Repository로 생성
- 1주차 결과물을 조별 Repository에 Push
- GitHub에서 `week1` 폴더가 표시되는지 확인

### 필수 2. Branch 기반 작업

각 조원은 자신의 역할에 맞는 Branch를 생성하여 작업합니다.

```text
feature/preprocessing
feature/logistic-regression
feature/random-forest
feature/evaluation-metrics
```

GitHub 또는 터미널에서 Branch가 4개 이상 생성되었는지 확인합니다.

### 필수 3. Pull Request 및 Code Review

- 조원 전원이 자신의 작업 Branch로 PR 생성
- `base: main` / `compare: 작업 Branch` 확인
- 각 PR에 최소 1건 이상의 Review Comment 작성
- 다른 조원의 변경사항을 확인한 뒤 Review 진행

### 필수 4. 모든 PR Merge

- Review가 완료된 PR을 `main`에 Merge
- 모든 기능 Branch의 변경사항이 `main`에 반영되었는지 확인
- Merge가 완료된 PR 화면을 확인

### 필수 5. Merge Conflict 발생 및 해결

- 같은 파일의 같은 부분을 서로 다르게 수정하여 Conflict 발생
- Conflict Marker 확인
- 유지할 코드를 선택하거나 변경사항을 조합하여 해결
- 해결 후 Commit 및 Push

예시:

```bash
git add app.py
git commit -m "fix: resolve merge conflict"
git push
```

---

## 4. 심화 체크포인트 상세

### 심화 1. Issue 생성 및 Commit Convention 적용

GitHub Issue를 생성하고 Commit Message에 Issue 번호를 연결합니다.

예시:

```text
docs: update week2 README (#1)
```

Commit Message는 다음 형식을 사용합니다.

```text
<type>: <summary>
```

예시 Type:

- `feat`: 기능 추가 또는 개선
- `fix`: 오류 수정
- `docs`: 문서 수정
- `refactor`: 코드 구조 개선
- `chore`: 설정 및 기타 작업

Commit Convention은 `CONTRIBUTING.md`에 문서화합니다.

### 심화 2. PR Template 작성 및 적용

다음 경로에 PR Template을 생성합니다.

```text
.github/pull_request_template.md
```

새로운 PR 생성 시 Template이 자동으로 표시되는지 확인합니다.

### 심화 3. Branch Protection 설정 및 동작 확인

`main` Branch를 대상으로 Ruleset을 설정합니다.

권장 설정:

```text
Enforcement status: Active
Target branch: main
Require a pull request before merging
Required approvals: 1
```

Review 승인 전에는 Merge가 제한되고, 다른 조원의 Approval 이후 Merge가 가능한지 확인합니다.

---

## 5. 최종 완료 기준

### 필수

- [ ] 조별 Repository 생성 및 1주차 결과물 Push
- [ ] 조원별 Branch 생성 및 작업
- [ ] 조원 전원 PR 생성 및 Review Comment 작성
- [ ] 모든 PR Merge
- [ ] Merge Conflict 발생 및 해결

### 심화

- [ ] Issue와 Commit 연결 및 Commit Convention 적용
- [ ] PR Template 적용
- [ ] Branch Protection 적용 및 동작 확인
