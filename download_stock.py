import yfinance as yf
import pandas as pd

stocks = ["8591.T","8593.T", "3850.T", "8058.T", "8316.T", "8766.T", "1928.T", "8098.T", "2914.T", "9434.T"]

csv = []

for stock in stocks:
    name = yf.Ticker(stock) #銘柄の情報を取得
    data = name.history(period="1y", interval="1d") #データをダウンロード
    data["Ticker"] = stock
    csv.append(data)

pd.concat(csv).to_csv("stock_data.csv") #データをCSVファイルに保存
print(data.index)
print("データ件数:", len(data))