from bs4 import BeautifulSoup
import asyncio
import aiohttp
from requests import request
from collections import defaultdict
import re
import pandas as pd

home_page = "https://markets.businessinsider.com/index/components/s&p_500"

parsed_company_pages = []
prepared_companies = defaultdict(dict)


async def main():
    tasks = list()
    await parse(home_page)
    counter = 0
    i = 1
    while True:
        page = await parse(home_page + f"?p={i}")
        if page.table is None:
            print(counter, "parsed companies on", i - 1, "pages was founded")
            break
        links = page.find("table", class_="table table-small").find_all("a")
        for row in links:
            company_url = "https://markets.businessinsider.com" + row["href"]
            growth_element = row.findParent().findParent().find_all("span")[-2]
            growth = float(growth_element.text.replace(",", ""))
            prepared_companies[company_url]["growth"] = growth
            tasks.append(parse(company_url))
            counter += 1
        i += 1
        break
    await asyncio.gather(*tasks)


async def parse(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            parsed_page = BeautifulSoup(await response.text(), "html.parser")
            add_page_to_companies(url, parsed_page)
            return parsed_page


def add_page_to_companies(url, page):
    if not url.startswith(home_page):
        parsed_company_pages.append(page)


def check_exchange():
    page = request("get", "http://www.cbr.ru/scripts/XML_daily.asp")  # config???
    exchange = BeautifulSoup(page.text, "html.parser").find("valute", id="R01235")
    return float(exchange.value.text.replace(",", "."))


def preparing_companies():
    exchange = check_exchange()
    for company in parsed_company_pages:
        company_url = company.find("link", rel="canonical")["href"]
        preparing_company = prepared_companies[company_url]

        company_code_element = company.findChild(class_="price-section__category")
        preparing_company["code"] = company_code_element.span.text[2:]

        company_name_element = company.findChild(class_="price-section__label")
        preparing_company["first_name"] = company_name_element.text

        price_element = company.findChild(class_="price-section__current-value")
        price = float(price_element.text.replace(",", "") * exchange)
        if price:
            preparing_company["price"] = price

        p_e_header = company.find(class_="snapshot__header", text="P/E Ratio")
        if p_e_header:
            p_e_value = float(p_e_header.findParent().text.split()[0])
            preparing_company["P/E"] = p_e_value

        def get_52weeks_value(element):
            return float(element[0].split()[1].strip(","))

        high52weeks_element = re.findall(
            r"high52weeks:.{2,}", str(company.find_all("script"))
        )
        high52weeks = get_52weeks_value(high52weeks_element)

        low52weeks_element = re.findall(
            r"low52weeks:.{2,}", str(company.find_all("script"))
        )
        low52weeks = get_52weeks_value(low52weeks_element)

        if low52weeks > 0 and high52weeks > 0:
            preparing_company["potential profit"] = high52weeks / low52weeks * exchange

    return prepared_companies


def make_output(data):
    data_from_companies = pd.DataFrame(data.values())
    with open("price.json", "w") as f:
        price_from_pandas = data_from_companies.nlargest(10, "price")
        f.write(price_from_pandas.to_json(orient="index").strip("'"))

    with open("p_div_e.json", "w") as f:
        p_div_e_from_pandas = data_from_companies.nsmallest(10, "P/E")
        f.write(p_div_e_from_pandas.to_json(orient="index"))

    with open("growth.json", "w") as f:
        growth_from_pandas = data_from_companies.nlargest(10, "growth")
        f.write(growth_from_pandas.to_json(orient="index"))

    with open("potential profit.json", "w") as f:
        profit_frpm_pandas = data_from_companies.nlargest(10, "potential profit")
        f.write(profit_frpm_pandas.to_json(orient="index"))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
make_output(preparing_companies())
