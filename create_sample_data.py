import pandas as pd

# ایجاد داده‌های فرضی
dates = pd.date_range(start='2020-01-01', periods=36, freq='M')  # دقیقاً ۳۶ ماه
prices = [450000, 460000, 470000, 480000, 490000, 500000, 510000, 520000, 530000, 540000, 
          550000, 560000, 570000, 580000, 590000, 600000, 610000, 620000, 630000, 640000,
          650000, 660000, 670000, 680000, 690000, 700000, 710000, 720000, 730000, 740000,
          750000, 760000, 770000, 780000, 790000, 800000]

# بررسی طول آرایه‌ها
print(f"Length of dates: {len(dates)}")
print(f"Length of prices: {len(prices)}")

data = pd.DataFrame({'date': dates, 'price': prices})
data.to_csv('sample_pistachio_prices.csv', index=False)
