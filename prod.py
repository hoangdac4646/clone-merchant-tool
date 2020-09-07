from typing import List

from variable import Variables


class ProdVariables(Variables):
    domain = 'https://inside.dev.meete.co'

    #User
    username = "tu"
    password = "123456"

    merchant_ids: List[int] = [222]
    place_ids: List[int] = []