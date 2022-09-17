import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver")

driver.get("https://www.coinglass.com/zh/AccumulatedFundingRate")

driver.find_element_by_xpath("//*[@id='__next']/div/div[4]/div[2]/main/div/div[3]/div/div[3]").click()
driver.implicitly_wait(10)

    # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[4]/div[2]/main/div/div[3]/div/div[3]")))
#

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
    if i == 10:
        break

# print(df.head())
df.to_csv("table1.csv", index=False)

columns_div2 = driver.find_elements(By.CSS_SELECTOR, "#cfrtop .bybt-font-mini")
# print(columns_div)
columns2 = [div.text for div in columns_div2 if div.text != ""]
# print(columns2)
df2 = pd.DataFrame(columns=["symbol", *columns2, "CoinEx"])
value_rows_div_all_2 = driver.find_elements(By.XPATH, '//*[@id="cfr"]/div')
for i, value_row_div_2 in enumerate(value_rows_div_all_2):
    # print(value_row_div)
    # print("printing_rows...")
    value_row_div_child = value_row_div_2.find_elements(By.XPATH, './*')
    value_rows = [div.text for div in value_row_div_child if div.text != ""]
    # print(len(value_rows))
    df2.loc[df2.shape[0]] = [rows[i], *value_rows]
    if i == 10:
        break

# print(df2.head())
df2.to_csv("table2.csv", index=False)

writer = pd.ExcelWriter('CoinGlassRate.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df.to_excel(writer, sheet_name='USDT或USD合约', index=False)
df2.to_excel(writer, sheet_name='币本位合约', index=False)
# Close the Pandas Excel writer and output the Excel file.
writer.save()
