# Git/GitHub 협업 규칙

이 문서는 2주차 실습에서 사용하는 최소 협업 규칙이다.

## 1. 작업 전 main 동기화

```bash
git switch main
git pull origin main
```

## 2. 개인 branch 생성

```bash
git switch -c feature/<작업명>
```

예시:

- `feature/preprocessing`
- `feature/logistic-regression`
- `feature/random-forest`
- `feature/evaluation-metrics`

## 3. 변경 확인 및 commit

```bash
git status
git diff
git add <수정한 파일>
git commit -m "feat: 작업 내용"
```

## 4. push 및 Pull Request

```bash
git push -u origin <branch-name>
```

GitHub에서 main을 대상으로 Pull Request를 생성하고 다른 조원에게 review를 요청한다. 자신의 Pull Request를 바로 merge하지 않는다.

## 5. Merge Conflict 처리

충돌이 발생하면 `<<<<<<<`, `=======`, `>>>>>>>` 사이에서 사용할 최종 코드를 조원과 결정한다. 표시를 제거한 뒤 다음과 같이 반영한다.

```bash
git add <충돌을 해결한 파일>
git commit -m "fix: resolve merge conflict"
git push
```

충돌의 목적은 한 사람의 코드를 선택하는 것이 아니라, 두 변경의 의도를 확인하고 정상 동작하는 하나의 결과로 통합하는 것이다.
