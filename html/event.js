    const search = document.getElementById('search');
    const search_value = document.getElementById('search_value');
    const file_name = document.getElementById('file_name');

    // 検索ボタン押下時のイベント
    search.addEventListener('click', () => {
        if(file_name.value === "") {
            alert('CSVファイル名を入力してください。');
            return;
        }
        if(search_value.value === "") {
            alert('検索キーワードを入力してください。');
            return;
        }
        kimetsu_search(file_name.value,search_value.value);
        return
    })

    eel.expose(view_log_js);

    // Python処理から呼び出す
    function view_log_js(log) {
        console.log(log);
        document.getElementById('serach_result').value += log + "\n";
    }

    // Python側メソッドを呼び出す
    async function kimetsu_search(file_name,search_value) {
        await eel.kimetsu_search(file_name,search_value)();
        return result;
    }