import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# بارگذاری داده‌ها
data = pd.read_csv('sample_pistachio_prices.csv', parse_dates=['date'], index_col='date')
prices = data['price']

# آموزش مدل ARIMA
model = ARIMA(prices, order=(1, 1, 1))  # تنظیمات اولیه
fitted_model = model.fit()

# پیش‌بینی ۱۲ ماه آینده
forecast = fitted_model.forecast(steps=12)

# مصورسازی
plt.plot(prices, label='داده‌های واقعی')
plt.plot(forecast, label='پیش‌بینی', linestyle='--')
plt.title('پیش‌بینی قیمت پسته')
plt.xlabel('تاریخ')
plt.ylabel('قیمت (تومان)')
plt.legend()
plt.show()