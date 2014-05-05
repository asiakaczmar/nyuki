from itertools import izip_longest



def get_words_with_max_distance(word, words_to_cmp, max_distance):
    found = []
    prebuilt = [range(len(word) + 1)]
    previous_word_to_cmp = ""
    for current_word_to_cmp in words_to_cmp:
        prebuilt = get_levenshtein_table(word, previous_word_to_cmp,
                                         current_word_to_cmp, prebuilt)
        if prebuilt[-1][-1] <= max_distance:
            found.append(current_word_to_cmp)
        previous_word_to_cmp = current_word_to_cmp
    return found


def get_levenshtein_table(word, previous_cmp_word, current_cmp_word, prebuilt):
    index = get_diff_index(previous_cmp_word, current_cmp_word)

    return build_levenshtein_table(prebuilt[:index+1], word,
                                   current_cmp_word[index:])


def get_diff_index(word1, word2):
    for index, (letter1, letter2) in enumerate(izip_longest(word1, word2)):
        if letter1 != letter2:
            return index


def build_levenshtein_table(prebuilt, word, ending):
    for letter in ending:
        add_row(prebuilt, word, letter)
    return prebuilt


def add_row(prebuilt, word, letter):
    current_row = len(prebuilt)
    word_len = len(prebuilt[0])
    prebuilt.append([])

    prebuilt[current_row].append(prebuilt[current_row-1][0] + 1)
    for x in range(1, word_len):
        insert_cost = prebuilt[current_row][x-1] + 1
        delete_cost = prebuilt[current_row-1][x] + 1
        substitute_cost = prebuilt[current_row-1][x-1]
        if word[x-1] != letter:
            substitute_cost += 2
        prebuilt[current_row].append(
            min(insert_cost, delete_cost, substitute_cost))

    return prebuilt

