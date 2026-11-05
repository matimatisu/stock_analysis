import yfinance as yf
import pandas as pd

stocks = ["7203.T","6758.T", "9984.T", "9432.T", "8306.T", "8316.T", "6861.T", "6954.T", "7974.T", "4502.T"]

csv = []

for stock in stocks:
    name = yf.Ticker(stock) #銘柄の情報を取得
    data = name.history(period="1y", interval="1d") #データをダウンロード
    data["Ticker"] = stock
    csv.append(data)

pd.concat(csv).to_csv("stock_data.csv") #データをCSVファイルに保存
print(data.index)
print("データ件数:", len(data))