# github action
[![data_crawler](https://github.com/n3n33/github-action/actions/workflows/main.yml/badge.svg)](https://github.com/n3n33/github-action/actions/workflows/main.yml)
### workflows
github workflow 안에 yaml 파일을 따라 workflow 생성함
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name : set up python
        uses: actions/setup-python@v2
        with:
          python-version: 3.7
      - name: Install Dependency
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Get Hadoop Release Note Contents
        run: |
          python main.py
        env:
          GIT_ACTION_SECRET: ${{ secrets.GIT_ACTION_SECRET}}   
```
### get_releasenote.py
하둡 릴리즈 노트에서 주요 부분 크롤링하여 해당 문구들 리턴

### git
워크플로우 생성된 깃 레포지토리 정보
이슈 등록위함

### main
하둡 릴리즈 노트 크롤링하는 함수 불러와 실행
레포지토리 정보와 이슈 등록하기 위한 함수 불러와 실행




