import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("stock_data.csv")

print("[株価データの先頭5行]")
print(df.head())

print("\n[終値の分析]")
print("最高値:", df['Close'].max())
print("最低値:", df['Close'].min())
print("平均値:", df['Close'].mean())

df["Close"].plot(title="Toyota Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
# グラフを画像ファイルとして保存する
plt.tight_layout()
plt.savefig("stock_chart.png")
plt.close()

