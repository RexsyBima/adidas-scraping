from src.utils import get_soup
from src.models import Category, Product
import json


def main():
    url = "https://www.adidas.co.id/graphql?hash=1081972869&_filter_0={sku:{eq:JQ8757},customer_group_id:{eq:0}}"
    data = get_soup(url)
    # print(data)
    # with open("data.json", "w") as f:
    #     json.dump(data, f)
    product = Product(
        id=1,
        name=data["data"]["products"]["items"][0]["name"],
        sku=data["data"]["products"]["items"][0]["sku"],
        price=data["data"]["products"]["items"][0]["price_range"]["minimum_price"]["final_price"]["value"],
        category=Category.SHOES,
        release_date=data["data"]["products"]["items"][0]["custom_attributes"]["launch_date"]["value"]
    )
    print(product)
    with open("product.json", "w") as f:
        product = product.model_dump()
        product["category"] = product["category"].value
        product["release_date"] = product["release_date"].strftime(
            "%Y-%m-%d %H:%M:%S")
        json.dump(product, f)


if __name__ == "__main__":
    main()
