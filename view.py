import eel
import desktop
import search

app_name = "html"
end_point = "index.html"
size = (700, 600)


@eel.expose
def kimetsu_search(filename, search_value):
    """
    引数filenameにsearch_value値があるか検索して、結果を返す（javascript連携用）

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
    result = search.kimetsu_search(filename, search_value)
    return result


desktop.start(app_name, end_point, size)
# desktop.start(size=size,appName=app_name,endPoint=end_point)
