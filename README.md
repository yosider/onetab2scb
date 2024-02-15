このPythonスクリプトは、OneTabエクスポートファイルを処理し、指定された行数でページを分割し、Scrapboxのインポート用のJSON形式で出力します。

## 使い方

1. レポジトリをcloneしてください

3. スクリプトを次のように実行します：

```bash
python main.py <filepath> [-o <output>] [-n <num_line_per_page>]
```

ここで、
- `<filepath>` はOneTabエクスポートファイルへのパスです。
- `<output>` は出力ファイルの名前です（デフォルトは "import.json"）。filepathと同じディレクトリに作成されます。
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
- `<filename>` は入力ファイル名（拡張子なし）です。
- `<page_number>` はページ番号です（1から始まります）。
- `<lines>` はそのページの行のリストです。
