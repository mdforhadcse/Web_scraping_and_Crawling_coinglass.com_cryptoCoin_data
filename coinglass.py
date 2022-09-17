import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("chromedriver")
driver.get("https://www.coinglass.com/zh/AccumulatedFundingRate")

rows_divs = driver.find_elements(By.XPATH,
                                 "//*[@id='__next']/div/div[4]/div[2]/main/div/div[5]/div[1]/div[3]/div[1]/div")
# print(rows_divs)
rows = [div.text for div in rows_divs if div.text != ""]
# print(rows)

# columns_div1 = driver.find_elements(By.CSS_SELECTOR, "#utop .bybt-font-mini")
columns_div1 = driver.find_elements(By.XPATH, '//*[@id="ufrtop"]/div/div')

# print(columns_div)
columns1 = [div.text for div in columns_div1 if div.text != ""]
# print(columns1)
# print(len(columns1))
df = pd.DataFrame(columns=["symbol", *columns1, "Gate", "Bitget", "CoinEx"])

value_rows_div_all = driver.find_elements(By.XPATH, '//*[@id="ufr"]/div')
for i, value_row_div in enumerate(value_rows_div_all):
    # print(value_row_div)
    # print("printing_rows...")
    value_row_div_child = value_row_div.find_elements(By.XPATH, './*')
    value_rows = [div.text for div in value_row_div_child if div.text != ""]
    # print(len(value_rows))
    df.loc[df.shape[0]] = [rows[i], *value_rows]


# # print(df.head())
# df.to_csv("table1.csv", index=False)

button_7days = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[4]/div[2]/main/div/div[3]/div/div[3]"))).click()
driver.implicitly_wait(10)
rows_divs7 = driver.find_elements(By.XPATH,
                                 "//*[@id='__next']/div/div[4]/div[2]/main/div/div[5]/div[1]/div[3]/div[1]/div")
# print(rows_divs)
rows7 = [div.text for div in rows_divs7 if div.text != ""]
# print(rows)

# columns_div1 = driver.find_elements(By.CSS_SELECTOR, "#utop .bybt-font-mini")
columns_div7 = driver.find_elements(By.XPATH, '//*[@id="ufrtop"]/div/div')

# print(columns_div)
columns7 = [div.text for div in columns_div7 if div.text != ""]
# print(columns1)
# print(len(columns1))
df7 = pd.DataFrame(columns=["symbol", *columns7, "Gate", "Bitget", "CoinEx"])

value_rows_div_all7 = driver.find_elements(By.XPATH, '//*[@id="ufr"]/div')
for i, value_row_div in enumerate(value_rows_div_all7):
    # print(value_row_div)
    # print("printing_rows...")
    value_row_div_child7 = value_row_div.find_elements(By.XPATH, './*')
    value_rows7 = [div.text for div in value_row_div_child7 if div.text != ""]
    # print(len(value_rows))
    df7.loc[df7.shape[0]] = [rows7[i], *value_rows7]






button_30days = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[4]/div[2]/main/div/div[3]/div/div[4]"))).click()
driver.implicitly_wait(10)
rows_divs30 = driver.find_elements(By.XPATH,
                                 "//*[@id='__next']/div/div[4]/div[2]/main/div/div[5]/div[1]/div[3]/div[1]/div")
# print(rows_divs)
rows30 = [div.text for div in rows_divs30 if div.text != ""]
# print(rows)

# columns_div1 = driver.find_elements(By.CSS_SELECTOR, "#utop .bybt-font-mini")
columns_div30 = driver.find_elements(By.XPATH, '//*[@id="ufrtop"]/div/div')

# print(columns_div)
columns30 = [div.text for div in columns_div30 if div.text != ""]
# print(columns1)
# print(len(columns1))
df30 = pd.DataFrame(columns=["symbol", *columns30, "Gate", "Bitget", "CoinEx"])

value_rows_div_all30 = driver.find_elements(By.XPATH, '//*[@id="ufr"]/div')
for i, value_row_div in enumerate(value_rows_div_all30):
    # print(value_row_div)
    # print("printing_rows...")
    value_row_div_child30 = value_row_div.find_elements(By.XPATH, './*')
    value_rows30 = [div.text for div in value_row_div_child30 if div.text != ""]
    # print(len(value_rows))
    df30.loc[df30.shape[0]] = [rows30[i], *value_rows30]




writer = pd.ExcelWriter('Task2-CoinglassRate.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df.to_excel(writer, sheet_name='单所1日', index=False)
df7.to_excel(writer, sheet_name='单所7日', index=False)
df30.to_excel(writer, sheet_name='单所30日', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
