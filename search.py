import pandas as pd
import os

### デスクトップアプリ作成課題
def kimetsu_search(filename,search_value):
    """
    引数filenameにsearch_value値があるか検索して、結果を返す

    Parameters
    ----------
    filename : string
        検索対象のファイル名。
    search_value : string
        検索対象の文字列。

    Returns
    -------
    kimetsu_search : string
        検索結果。
    """
    # ファイル存在チェック
    if not os.path.isfile(filename):
        return f"『CSVファイル：{filename}』はありません。"

    # 検索対象取得
    df=pd.read_csv(f"./{filename}")
    source=list(df["name"])

    # 検索判定
    if search_value in source:
        return "『{}』はあります".format(search_value)
    else:
        return "『{}』はありません".format(search_value)

