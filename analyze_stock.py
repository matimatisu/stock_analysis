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

#空のリスト作成
rank_list = [] #順位
stock_list = [] #株コード
dividends_list = [] #利回り

for number, result_stock in enumerate(result_sort, start=1):

    rank_list.append(number)
    stock_list.append(result_stock[0])
    dividends_list.append(result_stock[1])

data = dict((['順位',rank_list],['銘柄',stock_list],['利回り',dividends_list])) #辞書型に変更
print(data)

# three%_yield =[]

# for x in stock_list:
#    three%_yield = df[df["Ticker"] == stock_list(x)]

data_tabel = pd.DataFrame(data) #表に変換

data_tabel.to_csv("pandas_output.csv",index=False, encoding="utf-8-sig") #CSV保存

five_moving_average_line = df["Close"].rolling(window=5).mean()
tf_moving_average_line = df["Close"].rolling(window=25).mean()

df["MA5"] = five_moving_average_line #dfにMA5の5日平均値を追加
df["MA25"] = tf_moving_average_line #dfにMA25の25日平均値を追加
print(df.tail(10))

df["Close"].plot(label="closing price") #終値の折れ線グラフを表示
df["MA5"].plot(label="5-day moving average")
df["MA25"].plot(label="25-day moving average")



plt.legend()#折れ線グラフの説明の表示

plt.xlabel("Date")
plt.ylabel("Price")
# グラフを画像ファイルとして保存する
plt.tight_layout()
plt.savefig("stock_chart.png")
plt.close()