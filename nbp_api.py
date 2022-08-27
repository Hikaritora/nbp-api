from bdb import effective
import requests
import datetime
import matplotlib.pyplot as plt
import time
import matplotlib.dates as mdates

currency = "USD"
start_date = "2021-07-01"
end_date = "2022-07-01"

start_date2 = start_date.split("-")
end_date2 = end_date.split("-")


d1 = datetime.date(int(start_date2[0]), int(start_date2[1]), int(start_date2[2]))
d2 = datetime.date(int(end_date2[0]), int(end_date2[1]), int(end_date2[2]))

difference = d2 - d1
#assert difference.days <= 93, "Za duzy przedzial czasowy, przekracza 93 dni. "

link = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{start_date}/{end_date}/"

dates = []
exchange_rates = []

# for i in kurs["rates"]:
#     dates.append(i["effectiveDate"])
#     exchange_rates.append(i["mid"])


for i in range(1):
    time.sleep(1)
    kurs = requests.get(link).json()
    for i in kurs["rates"]:
        dates.append(i["effectiveDate"])
        exchange_rates.append(i["mid"])


currency2 = "EUR"
link2 = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency2}/{start_date}/{end_date}/"

dates2 = []
exchange_rates2 = []

time.sleep(3)

for i in range(1):
    time.sleep(1)
    kurs = requests.get(link2).json()
    for i in kurs["rates"]:
        dates2.append(i["effectiveDate"])
        exchange_rates2.append(i["mid"])
        
        
plt.plot(dates, exchange_rates, label=f"{currency} exchange rate")
plt.plot(dates, exchange_rates2, label=f"{currency2} exchange rate")
plt.xlabel("Dates")
plt.ylabel("Exchange rates")
plt.title(f"Exchange rates of {currency} between {start_date} and {end_date} ")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=7))
ax.legend()
ax.grid(True)
plt.show()