from blog.models import ProdJSON
import json

products = ProdJSON.objects.filter()

obj = {
    "id" : "id",
    "site_id": "site_id",
    "title": "title",
    "date_created": "date_created",
    "last_updated": "last_updated",
    "price": "price",
    "currency_id": "currency_id",
    "permalink": "permalink",
    "thumbnail": "thumbnail",
    "secure_thumbnail": "secure_thumbnail"
    # "pictures[0].url": "picture"
    }

for i in range(0, products.count()) :
    tmp_json = json.loads(products[i].json_full_info)
    for k in obj.keys():
        products[i].json_basic_info[obj[k]] = tmp_json[k]

    products[i].json_basic_info['picture'] = tmp_json['pictures'][0]['url']

# print(products[i].json_full_info)
print(products[i].json_basic_info)




