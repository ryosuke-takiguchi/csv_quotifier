# scripts/io_handler.py
# このスクリプトは、CSVファイルの入出力処理を担当します。

import csv
from scripts.constants import DEFAULT_ENCODING, CSV_DELIMITER
from typing import List

class CSVIOHandler:
    @staticmethod
    def read_csv(file_path: str) -> List[List[str]]:
        with open(file_path, mode='r', encoding=DEFAULT_ENCODING, newline='') as f:
            return list(csv.reader(f, delimiter=CSV_DELIMITER))

    @staticmethod
    def write_csv(file_path: str, rows: List[List[str]]):
        with open(file_path, mode='w', encoding=DEFAULT_ENCODING, newline='') as f:
            writer = csv.writer(
                f,
                delimiter=CSV_DELIMITER,
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writerows(rows)