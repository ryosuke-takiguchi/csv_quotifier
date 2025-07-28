# scripts/constants.py
# このファイルは、CSVファイルの読み書きに使用される定数を定義しています。

# CSVファイルのデフォルト設定
# デフォルトの引用符文字、エンコーディング、区切り文字などを定義します。
DEFAULT_QUOTE_CHAR = '"'
DEFAULT_ENCODING = 'CP932'
CSV_DELIMITER = ','

# デフォルトの列インデックス
# CSVファイルの読み書き時にデフォルトで引用符を付ける列のインデックスを定義します。
# 列番号が0から始まることに注意してください。

DEFAULT_COLUMNS_TO_QUOTE = [1, 3]
