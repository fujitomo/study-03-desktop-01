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
    })

    //eel.expose(view_log_js);

    //function view_log_js(text) {
    //}

    // Python側メソッド呼び出し
    async function kimetsu_search(file_name,search_value) {
        let result = await eel.kimetsu_search(file_name,search_value)();
        console.log(result);
        document.getElementById('serach_result').value += result + "\n";
        return result;
    }