# scripts/config.py
# このファイルは、CSVファイルの読み書きに使用される設定を定義しています。

from scripts.constants import DEFAULT_QUOTE_CHAR

class QuoteConfig:
    def __init__(self, columns_to_quote: list[int], quote_char: str = DEFAULT_QUOTE_CHAR):
        self.columns_to_quote = columns_to_quote
        self.quote_char = quote_char