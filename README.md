# CSV Quotifier

CSVファイルの**指定列に文字列引用符（例："）を付与**するPythonツールです。  
GUIのファイル選択ダイアログとログ出力機能を備え、操作とトレースが簡単です。

---

## 🔧 主な機能

- CSVファイルの任意列に文字列引用符を追加
- tkinterダイアログでファイル選択可能
- ログファイルを `logs/` ディレクトリに自動出力
- シンプルなオブジェクト指向構成で拡張も容易

---

## 📁 ディレクトリ構成

```
csv_quotifier/
├── main.py
├── scripts/
│   ├── config.py          # 引用設定クラス
│   ├── constants.py       # 定数管理
│   ├── io_handler.py      # CSVの読み書き
│   ├── logger_setup.py    # ロガー構築
│   └── processor.py       # 引用符処理クラス
├── logs/                  # ログファイル出力先（自動生成）
└── requirements.txt
```

---

## 🖥️ 実行方法

### 1. 依存モジュールのインストール

```bash
pip install -r requirements.txt
```

> ※ 現状外部モジュールの使用は想定されていないためスキップ可能な手順です。

### 2. 実行

```bash
python main.py
```

### 3. 操作フロー

1. CSVファイルをダイアログで選択
2. 対象列（`constants.py` の `DEFAULT_COLUMNS_TO_QUOTE`）に引用符が付与された新CSVが作成されます
3. `logs/` に処理ログが出力されます

---

## ⚙️ 設定変更

### 対象列の変更

`scripts/constants.py` を編集してください：

```python
DEFAULT_COLUMNS_TO_QUOTE = [0, 2]  # 例：1列目と3列目
```

### 引用文字の変更

```python
DEFAULT_QUOTE_CHAR = "'"
```

---

## 📄 出力ファイル例

入力ファイル（例: `data.csv`）：
```
田中,営業,12345
佐藤,開発,67890
```

出力ファイル（`data_quoted.csv`）：
```
"田中",営業,"12345"
"佐藤",開発,"67890"
```
---

## 🛠️ 開発情報

- Python 3.10+
- GUI: tkinter（標準）
- ログ出力: `logging` モジュール使用

---

## 📬 ライセンス

このプロジェクトはMITライセンスのもとに公開されています。
