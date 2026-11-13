import pandas as pd
import matplotlib.pyplot as plt
import download_stock as ds
from pathlib import Path

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
data_tabel = pd.DataFrame(data) #表に変換
data_tabel.to_csv("pandas_output.csv",index=False, encoding="utf-8-sig") #CSV保存

#利回り3％以上の株のCloseを取得
filltered_df = df[df["Ticker"].isin(stock_list)]
close_data_df = filltered_df.pivot(index="Date",columns="Ticker",values="Close") #銘柄ごとに列を分ける

stock_table = pd.DataFrame(close_data_df)
stock_table.to_csv("close_out.csv", index=False, encoding="utf-8-sig")

print(close_data_df)

#株コードそれぞれの終値をグラフにする
for i in stock_list:
    five_moving_average_line = close_data_df[i].rolling(window=5).mean()
    close_data_df[i + "_MA5"] = five_moving_average_line #dfにMA5の5日平均値を追加

    tf_moving_average_line = close_data_df[i].rolling(window=25).mean()
    close_data_df[i + "_MA25"] = tf_moving_average_line #dfにMA25の25日平均値を追加

    close_data_df[i].plot(label=i + "_closing price") #終値の折れ線グラフを表示
    close_data_df[i + "_MA5"].plot(label=i + "_5-day moving average")
    close_data_df[i + "_MA25"].plot(label=i + "_25-day moving average")

    plt.legend()#折れ線グラフの説明の表示
    plt.xlabel(i + "_Date")    
    plt.ylabel(i + "_Price")
    
    # グラフを画像ファイルとして保存する
    plt.tight_layout()
    chart_dir = Path("chart_image") #画像の保存先ファイルの作成
    chart_dir.mkdir(exist_ok=True) #保存先のフォルダが存在するかの確認
    plt.savefig( chart_dir / f"{i}_stock_chart.png")
    plt.close()