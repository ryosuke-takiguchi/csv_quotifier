# scripts/postprocess.py
# このスクリプトは、CSVファイルの後処理を担当します。
# 特に、ダブルクオートの不正な使用を修正するための関数を提供します。

def postprocess_csv_file(file_path: str, DEFAULT_ENCODING: str):
    with open(file_path, 'r', encoding=DEFAULT_ENCODING) as f:
        content = f.read()

    # """ → " に置換（必要に応じて注意深く）
    fixed_content = content.replace('"""', '"') 

    with open(file_path, 'w', encoding=DEFAULT_ENCODING) as f:
        f.write(fixed_content)
