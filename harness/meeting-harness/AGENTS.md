# Meeting Harness

## 목적

이 프로젝트는 회의록에서 `할 일:`로 시작하는 줄의 작업 내용을 추출하는 작은 Python 앱입니다. 동작은 `requirements.md`를 기준으로 합니다.

## 수정 규칙

- 앱 코드 수정은 `src/actions.py`로만 제한합니다.
- `tests/`, `demo.py`, `requirements.md`는 수정하지 않습니다.
- 변경 전 요구사항과 관련 코드를 확인하고, 변경 범위를 작게 유지합니다.
- 검사 명령은 `python3 -m unittest discover -s tests -v`와 `python3 demo.py`입니다.
- 완료 보고에는 실제 실행한 검사 결과와 변경 파일을 적습니다. 실행하지 않은 검사는 성공으로 보고하지 않습니다.
- 이 규칙 파일은 프로젝트 작업 지침일 뿐, 도구 권한이나 파일시스템 권한을 강제로 제한하지 않습니다.
