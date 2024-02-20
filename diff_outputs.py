import pandas as pd

# 2つのCSVファイルのパス
csv_file_path1 = "output1.csv"
csv_file_path2 = "output2.csv"

# CSVファイルをpandasのDataFrameに読み込む
df1 = pd.read_csv(csv_file_path1)
df2 = pd.read_csv(csv_file_path2)

# 同じnameを持つがpathが異なるエントリを抽出
different_path_same_name = pd.merge(df1, df2, on='name', how='inner', suffixes=('_output1', '_output2'))
different_path_same_name = different_path_same_name[different_path_same_name['path_output1'] != different_path_same_name['path_output2']]

# 出力先のCSVファイルに保存
different_path_same_name[['name', 'path_output1', 'path_output2']].to_csv("different_path_same_name_output.csv", index=False)

print("同じnameを持ちながらpathが異なるエントリ:")
print(different_path_same_name[['name', 'path_output1', 'path_output2']])