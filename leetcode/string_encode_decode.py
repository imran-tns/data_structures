from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for item in strs:
            encoded_string += f"{len(item)}#{item}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        str_list = []
        index = 0
        item_len = ""
        while len(s) > index:
            if s[index] == "#":
                item_len = int(item_len)
                item = s[index+1: index+1+item_len]
                str_list.append(item)
                index += item_len
                item_len = ""
            else:
                item_len += s[index]
            index += 1

        return str_list
