import xml.etree.ElementTree as ET
import csv

# XMLファイルのパス
xml_file_path = "local_manifest.xml"

# CSVファイルのパス
csv_file_path = "output2.csv"

# XMLファイルを読み込む
tree = ET.parse(xml_file_path)
root = tree.getroot()

# CSVファイルを書き込みモードで開く
with open(csv_file_path, 'w', newline='') as csvfile:
    # CSVファイルのヘッダーを定義
    fieldnames = ['path', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # ヘッダーを書き込む
    writer.writeheader()

    # XMLファイルからpathとnameを取得してCSVに書き込む
    for project in root.findall(".//project"):
        path = project.get("path")
        name = project.get("name")
        writer.writerow({'path': path, 'name': name})

print(f"CSVファイル '{csv_file_path}' に出力しました。")