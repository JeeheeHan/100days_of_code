def sort_sent(sent):
    """Return the sent in the given string, using temp sorted list thing to add words into the empty string"""
    s_list = sent.split()

    sort_s = sorted(s_list, key = lambda s:s[-1])

    answer = ""

    for n in sort_s:
        answer += n[:-1] + " "

    return answer[:-1]


def sor_sent2(sent):
    """Using empty list then join as string"""
    s_list = sent.split()

    answer = [] * len(s_list)

    for words in s_list:
        answer[int(words[-1]) - 1] = words[:-1]
    return " ".join(answer)

