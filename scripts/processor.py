# scripts/processor.py
# このスクリプトは、主処理クラスを定義し、CSVファイルの行に引用符を追加する機能を提供します。
# 引数として、configオブジェクトを受け取り、指定された列に引用符を追加します。

from scripts.config import QuoteConfig
from typing import List

class CSVQuoteProcessor:
    def __init__(self, config: QuoteConfig):
        self.config = config

    def quote_row(self, row: List[str]) -> List[str]:
        return [
            f'"{value}"' if i in self.config.columns_to_quote else value
            for i, value in enumerate(row)
        ]

    def quote_csv(self, rows: List[List[str]]) -> List[List[str]]:
        return [self.quote_row(row) for row in rows]
