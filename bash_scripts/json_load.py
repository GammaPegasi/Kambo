import json
# -*- coding: latin-1 -*-
import os, sys

obj = {
    "id": "MLA5782",
    "name": "Audi",
    "picture": 'null',
    "permalink": 'null',
    "total_items_in_this_category": 3578,
    "path_from_root": [
        {
            "id": "MLA1743",
            "name": "Autos, Motos y Otros"
        },
        {
            "id": "MLA1744",
            "name": "Autos y Camionetas"
        },
        {
            "id": "MLA5782",
            "name": "Audi"
        }
    ],
    "children_categories": [
        {
            "id": "MLA411502",
            "name": "80 Limousine",
            "total_items_in_this_category": 0
        },
        {
            "id": "MLA91018",
            "name": "A1",
            "total_items_in_this_category": 295
        },
        {
            "id": "MLA27485",
            "name": "A3",
            "total_items_in_this_category": 942
        },
        {
            "id": "MLA27452",
            "name": "A4",
            "total_items_in_this_category": 723
        },
        {
            "id": "MLA411490",
            "name": "A4 Allroad",
            "total_items_in_this_category": 24
        },
        {
            "id": "MLA412479",
            "name": "A4 Avant",
            "total_items_in_this_category": 24
        },
        {
            "id": "MLA50403",
            "name": "A5",
            "total_items_in_this_category": 331
        },
        {
            "id": "MLA27289",
            "name": "A6",
            "total_items_in_this_category": 87
        },
        {
            "id": "MLA412480",
            "name": "A6 Avant",
            "total_items_in_this_category": 0
        },
        {
            "id": "MLA117211",
            "name": "A7",
            "total_items_in_this_category": 28
        },
        {
            "id": "MLA50401",
            "name": "A8",
            "total_items_in_this_category": 3
        },
        {
            "id": "MLA29624",
            "name": "Allroad",
            "total_items_in_this_category": 42
        },
        {
            "id": "MLA51488",
            "name": "Cabrio",
            "total_items_in_this_category": 1
        },
        {
            "id": "MLA410856",
            "name": "Q2",
            "total_items_in_this_category": 55
        },
        {
            "id": "MLA117212",
            "name": "Q3",
            "total_items_in_this_category": 127
        },
        {
            "id": "MLA75127",
            "name": "Q5",
            "total_items_in_this_category": 329
        },
        {
            "id": "MLA99979",
            "name": "Q7",
            "total_items_in_this_category": 108
        },
        {
            "id": "MLA51467",
            "name": "R8",
            "total_items_in_this_category": 11
        },
        {
            "id": "MLA412481",
            "name": "R8 Coupé",
            "total_items_in_this_category": 10
        },
        {
            "id": "MLA412482",
            "name": "R8 Spyder",
            "total_items_in_this_category": 0
        },
        {
            "id": "MLA412483",
            "name": "RS3",
            "total_items_in_this_category": 9
        },
        {
            "id": "MLA36210",
            "name": "RS4",
            "total_items_in_this_category": 3
        },
        {
            "id": "MLA361676",
            "name": "RS5",
            "total_items_in_this_category": 8
        },
        {
            "id": "MLA47650",
            "name": "RS6",
            "total_items_in_this_category": 2
        },
        {
            "id": "MLA412484",
            "name": "RS6 Avant",
            "total_items_in_this_category": 0
        },
        {
            "id": "MLA412485",
            "name": "RS7 Sportback",
            "total_items_in_this_category": 0
        },
        {
            "id": "MLA27486",
            "name": "S3",
            "total_items_in_this_category": 114
        },
        {
            "id": "MLA27494",
            "name": "S4",
            "total_items_in_this_category": 46
        },
        {
            "id": "MLA83420",
            "name": "S5",
            "total_items_in_this_category": 18
        },
        {
            "id": "MLA411503",
            "name": "S5 Coupe",
            "total_items_in_this_category": 9
        },
        {
            "id": "MLA36184",
            "name": "S6",
            "total_items_in_this_category": 0
        },
        {
            "id": "MLA412486",
            "name": "S7",
            "total_items_in_this_category": 0
        },
        {
            "id": "MLA43560",
            "name": "S8",
            "total_items_in_this_category": 1
        },
        {
            "id": "MLA412487",
            "name": "SQ5",
            "total_items_in_this_category": 9
        },
        {
            "id": "MLA27495",
            "name": "TT",
            "total_items_in_this_category": 182
        },
        {
            "id": "MLA27480",
            "name": "Otros Modelos",
            "total_items_in_this_category": 27
        }
    ],
    "attribute_types": "attributes",
    "settings": {
        "adult_content": 'false',
        "buying_allowed": 'false',
        "buying_modes": [
            "classified"
        ],
        "catalog_domain": "MLA-CARS_AND_VANS",
        "coverage_areas": "not_allowed",
        "currencies": [
            "USD",
            "ARS"
        ],
        "fragile": 'false',
        "immediate_payment": "optional",
        "item_conditions": [
            "used",
            "not_specified",
            "new"
        ],
        "items_reviews_allowed": 'false',
        "listing_allowed": 'false',
        "max_description_length": 50000,
        "max_pictures_per_item": 15,
        "max_pictures_per_item_var": 6,
        "max_sub_title_length": 70,
        "max_title_length": 60,
        "maximum_price": 'null',
        "minimum_price": 'null',
        "mirror_category": 'null',
        "mirror_master_category": 'null',
        "mirror_slave_categories": [],
        "price": "required",
        "reservation_allowed": "mandatory",
        "restrictions": [],
        "rounded_address": 'false',
        "seller_contact": "optional",
        "shipping_modes": [
            "not_specified",
            "custom"
        ],
        "shipping_options": [],
        "shipping_profile": "not_allowed",
        "show_contact_information": 'true',
        "simple_shipping": "not_allowed",
        "stock": "required",
        "sub_vertical": "cars",
        "subscribable": 'false',
        "tags": [],
        "vertical": "motors",
        "vip_subdomain": "auto"
    },
    "meta_categ_id": 4870,
    "attributable": 'false'
}

print(json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))
