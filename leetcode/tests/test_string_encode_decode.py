from leetcode.string_encode_decode import Solution


def test_string_encode_decode():
    assert Solution().encode(["we", "say", ":", "yes"]) == "2#we3#say1#:3#yes"
    assert Solution().decode("2#we3#say1#:3#yes") == ["we", "say", ":", "yes"]

    assert Solution().encode([]) == ""
    assert Solution().decode("") == []

    assert Solution().encode(["neet", "code", "love", "you"]) == "4#neet4#code4#love3#you"
    assert Solution().decode("4#neet4#code4#love3#you") == ["neet", "code", "love", "you"]

    assert Solution().encode(["wearebatmanfaninbangladesh", "yes"]) == "26#wearebatmanfaninbangladesh3#yes"
    assert Solution().decode("26#wearebatmanfaninbangladesh3#yes") == ["wearebatmanfaninbangladesh", "yes"]