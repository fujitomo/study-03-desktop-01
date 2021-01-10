import eel
import desktop
import search

app_name = "html"
end_point = "index.html"
size = (700, 600)


@eel.expose
def kimetsu_search(filename, search_value):
    """
    引数filenameにsearch_value値があるか検索して、ログ出力する

    Parameters
    ----------
    filename : string
        検索対象のファイル名。
    search_value : string
        検索対象の文字列。
    """
    result = search.kimetsu_search(filename, search_value)
    # javascript処理を呼び出す
    eel.view_log_js(result)


desktop.start(app_name, end_point, size)
# desktop.start(size=size,appName=app_name,endPoint=end_point)
