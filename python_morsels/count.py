import re


def count_words(phrase):
    word_list = [word.casefold() for word in re.findall(r"\b[\w'-]+\b", phrase)]
    return {word: word_list.count(word) for word in word_list}

    # word_count = {}
    # for word in word_list:
    #     if word in word_count.keys():
    #         word_count[word] = word_count[word] + 1
    #     else:
    #         word_count.update({word: 1})
    # return word_count
