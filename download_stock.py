import yfinance as yf

stock = yf.Ticker("7203.T")

df = stock.history(period = "1y", interval = "1d")

df.to_csv("stock_data.csv")

print(df.head())

print("データ件数:", len(df))