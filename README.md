このPythonスクリプトは、OneTabエクスポートファイルを処理し、指定された行数でページを分割し、Scrapboxのインポート用のJSON形式で出力します。

## 使い方

1. 必要なパッケージをインストールします。以下のコマンドを実行してください。

```bash
pip install python-dotenv
```

2. `.env` ファイルを作成し、その中に `ROOT_PATH` 環境変数を設定します。これは、入力ファイルと出力ファイルが存在するディレクトリへのパスです。例えば、以下のように設定します：

```
ROOT_PATH=/path/to/your/directory
```

3. スクリプトを次のように実行します：

```bash
python main.py <filename> -o <output> --num_line_per_page <num_line_per_page>
```

ここで、
- `<filename>` はOneTabエクスポートファイルの名前です。
- `<output>` は出力ファイルの名前です（デフォルトは "import.json"）。
- `<num_line_per_page>` はページあたりの行数です（デフォルトは400）。

## 出力

出力ファイルは、Scrapboxのインポート用の次の形式のJSONです：

```json
{
  "pages": [
    {
      "title": "<filename> - <page_number>",
      "lines": [<lines>]
    },
    ...
  ]
}
```

ここで、
- `<filename>` は入力ファイルの名前（拡張子なし）です。
- `<page_number>` はページ番号です（0から始まります）。
- `<lines>` はそのページの行のリストです。
