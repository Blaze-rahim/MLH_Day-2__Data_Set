import csv
from datetime import datetime

path = "C:\\Users\\AbdulRahim\\Desktop\\New folder (3)\\Google Stock Market Data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)

data = []
for i in reader:
    # i is an list which is [dat,open,high,low,close,volmue , adj. close]
    date = datetime.strptime(i[0] , '%m/%d/%Y')
    openprice = float(i[1])
    high = float(i[2])
    low = float(i[3])
    close = float(i[4])
    vol = int(i[5])
    adj_close = float(i[6])

    data.append([date, openprice, high, low, close, vol, adj_close])

file.close()


#getting the daily stocks return

path = "C:\\Users\\AbdulRahim\\Desktop\\New folder (3)\\Dailyreturns.txt"
file = open(path, "w")
writer = csv.writer(file)
writer.writerow(["Date" , "Return"])

for i in range(len(data)-1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    dailyreturn = (todays_price - yesterdays_price) /  yesterdays_price
    writer.writerow([todays_date, dailyreturn])