from src.utils import get_soup
import sys
from src.models import Category, Product
import json
assert len(sys.argv) == 2, "Usage: python main.py <sku>"


def main():
    url = sys.argv[1]
    data = get_soup(url)
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
    print("data saved into product.json")


if __name__ == "__main__":
    main()
