# main.py
# このスクリプトは、エントリーポイントとして機能し、CSVファイルの引用符を処理するためのものです。

import os
from tkinter import Tk, filedialog
from scripts.config import QuoteConfig
from scripts.processor import CSVQuoteProcessor
from scripts.io_handler import CSVIOHandler
from scripts.logger_setup import setup_logger
from scripts.postprocess import postprocess_csv_file
from scripts.constants import DEFAULT_COLUMNS_TO_QUOTE
from scripts.constants import DEFAULT_ENCODING

def select_csv_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="CSVファイルを選択してください",
        filetypes=[("CSV Files", "*.csv")]
    )
    return file_path

def main():
    logger = setup_logger()

    input_file = select_csv_file()
    if not input_file:
        logger.warning("ファイルが選択されませんでした。処理を終了します。")
        return

    output_file = os.path.splitext(input_file)[0] + "_quoted.csv"

    config = QuoteConfig(DEFAULT_COLUMNS_TO_QUOTE)
    processor = CSVQuoteProcessor(config)

    try:
        rows = CSVIOHandler.read_csv(input_file)
        quoted_rows = processor.quote_csv(rows)
        CSVIOHandler.write_csv(output_file, quoted_rows)
        logger.info(f"変換完了: 出力ファイル -> {output_file}")
        postprocess_csv_file(output_file, DEFAULT_ENCODING)
        logger.info("後処理が完了しました。")
        
    except Exception as e:
        logger.exception(f"処理中にエラーが発生しました: {e}")

if __name__ == "__main__":
    main()