# adidas-scraping
Python program to scrape a adidas website using Python, Beautifulsoup4, and Curl_cffi. The output will be saved into file product.json
## Installation

Using virtual environment is recommended, then

```bash
pip install -r requirements.txt
```

## How to use
you must provide a url that has the json product 
[Like this (Check the url)](https://www.adidas.co.id/graphql?hash=1081972869&_filter_0={sku:{eq:JQ8757},customer_group_id:{eq:0}}). You can get them by using network tab inside a product and refresh it, then run
```bash
  python main.py "https://www.adidas.co.id/graphql?hash=1081972869&_filter_0={sku:{eq:JQ8757},customer_group_id:{eq:0}}"
```
