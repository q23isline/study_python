# study_python

[![LICENSE](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![GitHub Actions](https://github.com/q23isline/study_python/actions/workflows/ci.yml/badge.svg)](https://github.com/q23isline/study_python/actions/workflows/ci.yml)
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=555555&color=007acc&logoColor=007acc)](https://github.dev/q23isline/study_python)

[![Python](https://img.shields.io/static/v1?logo=python&label=Python&message=v3&labelColor=555555&color=#3776AB&logoColor=#3776AB)](https://www.python.org/)

Python 勉強用リポジトリ

## 前提

- インストール
  - [Windows Subsystem for Linux](https://learn.microsoft.com/ja-jp/windows/wsl/)
  - [Git](https://git-scm.com/)
  - [Docker Desktop](https://www.docker.com/ja-jp/products/docker-desktop/)
  - [Visual Studio Code](https://code.visualstudio.com/)

## はじめにやること

1. Windows Subsystem for Linux 上でプログラムダウンロード

    ```bash
    git clone https://github.com/q23isline/study_python.git
    ```

2. リポジトリのカレントディレクトリへ移動

    ```bash
    cd study_python
    ```

3. アプリ立ち上げ

    ```bash
    docker compose up -d
    ```

## 日常的にやること

### システム起動

```bash
docker compose up -d
```

### システム終了

```bash
docker compose down
```

## 動作確認

```bash
docker compose exec backend python3 shell/send_book_return_reminder_email_shell.py
```

## コード静的解析

```bash
# フォーマッター
docker compose exec backend autopep8 --diff --recursive .
docker compose exec backend black --diff .

# リンター
docker compose exec backend pylint ./
docker compose exec backend flake8
docker compose exec backend mypy ./
```
