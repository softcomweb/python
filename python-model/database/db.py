from . import common

# from typing import Dict
from boto3.dynamodb.conditions import Key, And

table = common.get_dynamodb_table()


def get_single_item(key, pk=None, sk=None):
    key_value = {}

    if pk:
        key_value[key] = pk

    if sk:
        key_value[sk] = sk

    print(key_value)

    item = table.get_item(Key=key_value).get("Item", [])

    return item


def put_single_item(item) -> bool:
    table.put_item(Item=item)
    return True

# def query_for_item(key, pk=None, sk=None, operation=None, query_str=None):
#   if operator:
#     key_condition_expression = And(
#       Key(pk).eq(key),
#       Key(sk).f"{operation}'(query_str)
#     )
#     item = table.query(
#       KeyConditionExpression=key_condition_expression
#     ).get("Items", [])

#     return item
