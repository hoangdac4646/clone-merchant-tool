from typing import List

from variable import Variables


class DevVariables(Variables):
    domain = 'https://inside.dev.meete.co'

    #User
    username = "tu"
    password = "123456"

    merchant_ids: List[int] = [226]
    place_ids: List[int] = [274]
