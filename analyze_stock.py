import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock_data.csv")
print(df.columns) #Divedends(配当金)の列があるかを確認

df["Date"] = pd.to_datetime(df["Date"]) #日付をdatetime型に変換

this_year = df["Date"].dt.year == 2026 #取り出す年を指定
total = df[this_year]["Dividends"].sum() #本年の配当金の合計を表示
latest_price = df.tail(1)['Close'].iloc[0]
dividends = total / latest_price * 100 #利回りの計算
print(dividends)

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