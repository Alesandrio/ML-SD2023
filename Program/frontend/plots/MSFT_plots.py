import pandas as pd
import matplotlib.pyplot as plt

# Config
name_company = f'Microsoft Corporation (MSFT)'

# Импорт данных
file_path_3_day = 'ML-SD2023\\Program\\data_predictions\\MSFT_3_day.csv'
file_path_7_day = 'ML-SD2023\\Program\\data_predictions\\MSFT_7_day.csv'
file_path_14_day = 'ML-SD2023\\Program\\data_predictions\\MSFT_14_day.csv'
file_path_31_day = 'ML-SD2023\\Program\\data_predictions\\MSFT_31_day.csv'
file_path_today = 'ML-SD2023\\Program\\data_predictions\\today.csv'
df_3_day = pd.read_csv(file_path_3_day)
df_7_day = pd.read_csv(file_path_7_day)
df_14_day = pd.read_csv(file_path_14_day)
df_31_day = pd.read_csv(file_path_31_day)
today_date = pd.read_csv(file_path_today)
today = today_date['date'].iloc[0]

#########################################################################################################
df_future = df_3_day
name_priod_company = f'{name_company} - прогноз на 3 дня'
fig, ax = plt.subplots(figsize=(11, 6))
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
train_end_date = pd.to_datetime(today)
ax.axvline(today, color='black', linestyle='--')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.title(name_priod_company, loc="center", size=18, weight='bold')
plot = {'fig': fig, 'ax': ax}
plt.show()
#########################################################################################################
df_future = df_7_day
name_priod_company = f'{name_company} - прогноз на 7 дней'
fig, ax = plt.subplots(figsize=(11, 6))
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
train_end_date = pd.to_datetime(today)
ax.axvline(today, color='black', linestyle='--')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.title(name_priod_company, loc="center", size=18, weight='bold')
plot = {'fig': fig, 'ax': ax}
plt.show()
#########################################################################################################
df_future = df_14_day
name_priod_company = f'{name_company} - прогноз на 14 дней'
fig, ax = plt.subplots(figsize=(11, 6))
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
train_end_date = pd.to_datetime(today)
ax.axvline(today, color='black', linestyle='--')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.title(name_priod_company, loc="center", size=18, weight='bold')
plot = {'fig': fig, 'ax': ax}
plt.show()
#########################################################################################################
df_future = df_31_day
name_priod_company = f'{name_company} - прогноз на 31 день'
fig, ax = plt.subplots(figsize=(10, 6))
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
plt.plot(df_future['date'], df_future['target'], label='Rate', color='blue', linewidth=3)
plt.plot(df_future['date'], df_future['predict'], label='Predict', color='red', linewidth=3)
train_end_date = pd.to_datetime(today)
ax.axvline(today, color='black', linestyle='--')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.title(name_priod_company, loc="center", size=18, weight='bold')
plot = {'fig': fig, 'ax': ax}
plt.show()