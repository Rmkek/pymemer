import vk_requests
import json
import random
import threading

groups = []  # String of group_id's
#  mine are '-73319310', '-73598440', '-28125083',
# '-66814271', '-55307799', '-66678575', '-45745333', '-95355317'
api = vk_requests.create_api(app_id='', login='', password='',
                             scope='messages')

user_array = ['224005125', '35933425']  # User id's array

_user_id = input("User that will be added into user_array.\n")

if _user_id == '\n' or ' ' or '-1':
    pass
else:
    user_array.append(_user_id)


def send_message(u_id, _attachment, _group_id, _post_id):  # method for sending posts
    api.messages.send(user_id=u_id, attachment=_attachment + _group_id + "_" + _post_id)

def get_post():
    group = groups[int(random.uniform(0, len(groups)))]  # random one group out of group array
    posts_amount = api.wall.get(owner_id=group, count='1')['count']  # get amount of posts in group
    offset = int(random.uniform(0, posts_amount))  # choose one post
    wall = api.wall.get(owner_id=group, count='1', offset=offset)  # get one post
    post_id = json.dumps(wall['items'][0]['id'])  # get this post id

    for u in user_array:  # send message to every user in array
        send_message(u, "wall", group, post_id)

    threading.Timer(5400.0, get_post).start()

get_post()