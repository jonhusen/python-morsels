def count_words(phrase):
    word_list = [word.strip(",;.!?").casefold() for word in phrase.split()]
    word_count = {word: word_list.count(word) for word in word_list}

    # word_count = {}
    # for word in word_list:
    #     if word in word_count.keys():
    #         word_count[word] = word_count[word] + 1
    #     else:
    #         word_count.update({word: 1})
    return word_count
