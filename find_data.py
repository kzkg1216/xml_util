import pandas as pd

# 2つのCSVファイルのパス
csv_file_path1 = "output2.csv"
csv_file_path2 = "output1.csv"

# CSVファイルをpandasのDataFrameに読み込む
df1 = pd.read_csv(csv_file_path1)
df2 = pd.read_csv(csv_file_path2)

# output1にはあるがoutput2にはないnameを抽出
only_in_output1 = df1[~df1['name'].isin(df2['name'])]

# 出力先のCSVファイルに保存
only_in_output1.to_csv("only_in_output1.csv", index=False)

print("output1にはあるがoutput2にはないname:")
print(only_in_output1)