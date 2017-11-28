import json
from pocket import Pocket, PocketException

consumer_key_file = open("../data/consumer-key", "r")
consumer_key = consumer_key_file.read()

access_token_file = open("../data/access-token", "r")
access_token = access_token_file.read()

tags_file = open("../data/tags.json", "r")
tags = json.loads(tags_file.read())
print(tags)

pocket_client = Pocket(
    consumer_key=consumer_key,
    access_token=access_token
)

try:
    # TODO
    # use given_title if not empty, otherwise fallback to resolved_title



    # data = pocket_client.retrieve(state="unread")
    # for key, value in data["list"].items():
    #     print("given_title: ", value["given_title"])
    #     print("resolved_title: ", value["resolved_title"])
    #     if "tags" in value:
    #         print("tags: ", value["tags"])
    #     print()
        
    # data = pocket_client.retrieve(state="unread", tag="inspiration")
    # for key, value in data["list"].items():
    #     print("given_title: ", value["given_title"])
    #     print("resolved_title: ", value["resolved_title"])
    #     print()

    pass

except PocketException as e:
    print(e.message)
