from urllib.request import urlopen
from bs4 import BeautifulSoup

# تعریف توابع برای بخش‌های اضافی
def get_price_ranking(text_ranking):
    return float(
        text_ranking.get_text().replace("$", "").replace("\n", "").replace(",", "")
    )

def get_name_ranking(text_name_rank):
    return text_name_rank.get_text().strip()

def get_price_market(text_market):
    return float(
        text_market.get_text().replace(",", "").replace("$", "").strip()
    )

def get_name_market(text_name_mark):
    return text_name_mark.get_text().strip()

# تعریف متغیرها برای منطق برنامه
address_coinranking = urlopen("https://coinranking.com/")
address_market = urlopen("https://coinmarketcap.com/")

coinranking_html = BeautifulSoup(address_coinranking.read(), "lxml")
coinmarket_html = BeautifulSoup(address_market.read(), "lxml")

# جستجوی  HTML مورد نظر
table_ranking = coinranking_html.find_all("div", class_="valuta")
table_market = coinmarket_html.find_all("div", class_="sc-a093f09c-0 gPTgRa")
name_ranking = coinranking_html.find_all("span", class_="profile__subtitle-name")
name_market = coinmarket_html.find_all("div", class_="sc-1c5f2868-3 dhNyQP")

# منطق برنامه
for i in range(10):
    # پردازش داده‌های coinranking
    price_name_ranking = get_name_ranking(name_ranking[i])
    price_ranking = get_price_ranking(table_ranking[2 * i])
    total_ranking = f"coinranking: {price_name_ranking} : {price_ranking}"
    print(total_ranking)
    print("-----------------------")

print("****************************************************************")

for i in range(10):
    # پردازش داده‌های coinmarketcap
    price_name_market = get_name_market(name_market[i])
    price_market = get_price_market(table_market[i])
    total_market = f"coinmarketcap: {price_name_market} : {price_market}"
    print(total_market)
    print("------------------------")

    # مقایسه قیمت‌ها
    if price_market > price_ranking:
        print(f"{total_market}  >  {total_ranking}")
    elif price_market < price_ranking:
        print(f"{total_ranking}  >  {total_market}")

# پایان برنامه
print("VA BELAKHARE TAMAM SHOD")