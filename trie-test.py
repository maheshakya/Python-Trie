def Trie_test():

    words = ['china', 'chinese', 'karate', 'chineses']

    S = Trie()

    for w in words:
        S.insert(w)

    S.dump()

    assert S.has_word('karate') is True
    assert S.has_word('karat') is False
    assert S.has_word('karatee') is False
    assert S.has_word('judo') is False

    assert S.has_prefix('kar') is True
    assert S.has_prefix('karr') is False
    assert S.has_prefix('kir') is False

if __name__ == '__main__':
    Trie_test()
