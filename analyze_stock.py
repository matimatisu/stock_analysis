import pandas as pd
import matplotlib.pyplot as plt
import download_stock as ds

df = pd.read_csv("stock_data.csv")
#print(df.columns) #Divedends(配当金)の列があるかを確認

result = []

for stock in ds.stocks: #stocksリストの中の銘柄を順番に取り出す
    stock_data = df[df["Ticker"] == stock].copy() #銘柄ごとのデータを取り出す

    stock_data["Date"] = pd.to_datetime(stock_data["Date"])#日付をdatetime型に変換
    this_year = stock_data["Date"].dt.year == 2026 #取り出す年を指定
    total = stock_data[this_year]["Dividends"].sum() #本年の配当金の合計を表示
    latest_price = stock_data.tail(1)['Close'].iloc[0]
    dividends = total / latest_price * 100 #利回りの計算

    if dividends >= 3.0:
        result.append((stock, dividends)) #利回り3%以上の銘柄をリストに追加

#利回りが高い順番に並べる
result_sort= sorted(result,key=lambda s:s[1] ,reverse=True)

d = dict(result_sort)


for number, result_stock in enumerate(result_sort, start=1):
    print(f"第:{number}, 銘柄:{result_stock[0]}, 利回り: {result_stock[1]:.2f}%")



# df["Price"] = pd.to_datetime(df["Price"]) #日付をdatetime型に変換
# this_year = df["Price"].dt.year == 2026 #取り出す年を指定
# total = df[this_year]["Dividends"].sum() #本年の配当金の合計を表示
# latest_price = df.tail(1)['Close'].iloc[0]
# dividends = total / latest_price * 100 #利回りの計算

# result = []
# if dividends >= 3.0:
#     result.append((ds.stock, dividends)) #利回り3%以上の銘柄をリストに追加

# for result_stock in result:
#     print(f"銘柄:{result_stock[0]}, 利回り: {result_stock[1]:.2f}%")


# print("[株価データの先頭5行]")
# print(df.head())

# print("\n[終値の分析]")
# print("最高値:", df['Close'].max())
# print("最低値:", df['Close'].min())
# print("平均値:", df['Close'].mean())

# df["Close"].plot(title="Toyota Stock Price")
# plt.xlabel("Date")
# plt.ylabel("Price")
# # グラフを画像ファイルとして保存する
# plt.tight_layout()
# plt.savefig("stock_chart.png")
# plt.close()