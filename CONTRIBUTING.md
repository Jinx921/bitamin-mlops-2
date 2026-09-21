# Contributing Guide

BITAMIN 17기 MLOps 세션 **2조**의 Git/GitHub 협업 규칙입니다.

본 프로젝트는 기능별 Branch에서 작업한 뒤, Commit → Push → Pull Request → Code Review → Merge 순서로 `main`에 반영합니다.

---

## 1. Basic Workflow

작업을 시작하기 전에 최신 `main`을 반영합니다.

```bash
git switch main
git pull origin main
```

새로운 작업은 별도의 Branch에서 진행합니다.

```bash
git switch -c <branch-name>
```

작업 후 변경사항을 확인합니다.

```bash
git status
git diff
```

변경사항을 Commit하고 Push합니다.

```bash
git add <file-name>
git commit -m "<commit-message>"
git push -u origin <branch-name>
```

이후 GitHub에서 Pull Request를 생성하고 다른 조원의 Review를 받은 뒤 `main`에 Merge합니다.

---

## 2. Branch Convention

기능별로 독립적인 Branch를 생성하여 작업합니다.

기본 형식:

```text
feature/<feature-name>
```

예시:

```text
feature/preprocessing
feature/logistic-regression
feature/random-forest
feature/evaluation-metrics
```

### Branch Rules

- 새로운 작업은 최신 `main`에서 시작합니다.
- `main`에서 직접 기능 개발을 진행하지 않습니다.
- 하나의 Branch에는 하나의 주요 작업 목적을 둡니다.
- Merge가 완료된 Branch는 필요에 따라 삭제할 수 있습니다.

---

## 3. Commit Message Convention

Commit Message는 다음 형식을 사용합니다.

```text
<type>: <summary>
```

### Type

| Type | Description | Example |
|---|---|---|
| `feat` | 새로운 기능 추가 또는 기능 개선 | `feat: add random forest model` |
| `fix` | 버그 및 오류 수정 | `fix: resolve merge conflict` |
| `docs` | README 등 문서 수정 | `docs: update week2 README` |
| `refactor` | 기능 변화 없이 코드 구조 개선 | `refactor: simplify preprocessing` |
| `chore` | 설정, 환경 등 기타 작업 | `chore: update .gitignore` |

### Examples

```text
feat: improve preprocessing
feat: improve logistic regression
feat: add random forest model
feat: add evaluation metrics
docs: update week2 README
fix: resolve merge conflict
chore: update .gitignore
```

### Commit Rules

- 하나의 Commit에는 하나의 작업 목적만 포함합니다.
- Commit Message만 보고 변경 내용을 파악할 수 있도록 작성합니다.
- Type은 소문자로 작성합니다.
- Summary는 짧고 명확하게 작성합니다.

---

## 4. Issue Linking

작업과 관련된 Issue가 있다면 Commit Message에 Issue 번호를 함께 작성할 수 있습니다.

예시:

```text
docs: update week2 README (#1)
```

Issue를 자동으로 닫고 싶다면 다음과 같은 키워드를 사용할 수 있습니다.

```text
fixes #1
closes #1
resolves #1
```

예시:

```text
docs: update week2 README, closes #1
```

---

## 5. Pull Request

작업 완료 후 GitHub에서 `main`을 대상으로 Pull Request를 생성합니다.

### PR Workflow

```text
Branch
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
Code Review
  ↓
Approve
  ↓
Merge
```

### PR Rules

- PR의 `base` Branch는 `main`으로 설정합니다.
- PR 제목만 보고 변경 내용을 파악할 수 있도록 작성합니다.
- 변경 내용과 확인 사항을 PR 본문에 간단하게 작성합니다.
- PR 작성자가 바로 Merge하지 않고 다른 조원의 Review를 먼저 받습니다.
- 각 PR에는 최소 1건 이상의 Review Comment를 남깁니다.
- Review가 완료된 후 Merge합니다.

---

## 6. Pull Request Template

PR 작성 형식을 통일하기 위해 다음 파일을 사용합니다.

```text
.github/pull_request_template.md
```

권장 형식:

```markdown
## 변경 내용
-

## 확인 사항
- [ ] 코드가 정상 실행되는지 확인했습니다.
- [ ] 관련 기능에 영향을 주지 않는지 확인했습니다.

## 기타
-
```

---

## 7. Merge Conflict

Merge Conflict가 발생하면 충돌한 Branch에서 최신 `main`을 반영합니다.

```bash
git switch <branch-name>
git fetch origin
git merge origin/main
```

Conflict Marker를 확인합니다.

```text
main Branch의 코드
```

유지할 코드를 선택하거나 두 변경사항을 적절히 조합한 뒤 Conflict Marker를 제거합니다.

해결 후:

```bash
git add <conflict-file>
git commit -m "fix: resolve merge conflict"
git push
```

같은 Branch에 Push하면 기존 Pull Request에 해결 결과가 자동으로 반영됩니다.

---

## 8. Review Checklist

PR Review 시 다음 항목을 확인합니다.

- 변경 목적이 명확한가?
- 불필요한 파일이 함께 수정되지 않았는가?
- 코드가 정상적으로 실행되는가?
- 기존 기능에 영향을 주지 않는가?
- Commit Message Convention을 지켰는가?
- 필요한 경우 관련 Issue가 연결되어 있는가?

---

## 9. Repository Rules

- `main`은 항상 실행 가능한 상태를 유지합니다.
- 새로운 기능은 별도의 Branch에서 작업합니다.
- 중요한 변경사항은 Pull Request와 Code Review를 거쳐 반영합니다.
- `.env`, 가상환경, 캐시, 로컬 설정 파일 등은 `.gitignore`로 관리합니다.
- 주차별 실습 결과와 체크포인트는 `weekN/README.md`에 정리합니다.
