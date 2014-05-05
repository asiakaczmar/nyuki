import unittest
from src.spellcheck.non_dict import (get_diff_index, add_row,
    build_levenshtein_table, get_levenshtein_table, get_words_with_max_distance)


class TestGetDiffIndex(unittest.TestCase):
    def test_short_long(self):
        result = get_diff_index("cat", "category")
        self.assertEqual(3, result)

    def test_long_short(self):
        result = get_diff_index("cat", "category")
        self.assertEqual(3, result)

    def test_different(self):
        result = get_diff_index("cathedral", "category")
        self.assertEqual(3, result)


class TestAddRow(unittest.TestCase):
    def test_add_different_letter(self):
        prebuilt = [[0, 1, 2, 3, 4]]
        result = add_row(prebuilt, "pony", "t")
        expected = [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5]]
        self.assertEqual(result, expected)

    def test_add_same_letter(self):
        prebuilt = [[0, 1, 2, 3, 4]]
        result = add_row(prebuilt, "pony", "p")
        expected = [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3]]
        self.assertEqual(result, expected)


class TestBuildLevenshteinTable(unittest.TestCase):
    def test_change_first(self):
        prebuilt = [[0, 1, 2, 3, 4]]
        result = build_levenshtein_table(prebuilt, "pony", "tony")
        expected = [
            [0, 1, 2, 3, 4],
            [1, 2, 3, 4, 5],
            [2, 3, 2, 3, 4],
            [3, 4, 3, 2, 3],
            [4, 5, 4, 3, 2],
        ]
        self.assertEqual(result, expected)

    def test_ending_not_bulit(self):
        prebuilt = [[0, 1, 2, 3, 4, 5]]
        result = build_levenshtein_table(prebuilt, "march", "may")
        expected = [
            [0, 1, 2, 3, 4, 5],
            [1, 0, 1, 2, 3, 4],
            [2, 1, 0, 1, 2, 3],
            [3, 2, 1, 2, 3, 4]
        ]
        self.assertEqual(result, expected)

    def test_ending_bulit(self):
        prebuilt = [[0, 1, 2, 3, 4, 5],
                    [1, 0, 1, 2, 3, 4],
                    [2, 1, 0, 1, 2, 3]]
        result = build_levenshtein_table(prebuilt, "march", "y")
        expected = [
            [0, 1, 2, 3, 4, 5],
            [1, 0, 1, 2, 3, 4],
            [2, 1, 0, 1, 2, 3],
            [3, 2, 1, 2, 3, 4]
        ]
        self.assertEqual(result, expected)


class TestGetLevenshteinTable(unittest.TestCase):
    def test_get_levenshtein_table(self):
        previous_prebuilt = [
            [0, 1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5, 6],
            [2, 3, 4, 3, 4, 5],
            [3, 4, 5, 4, 3, 4],
            [4, 5, 6, 5, 4, 5]
        ]
        result = get_levenshtein_table("clash", "base",
                                       "bash", previous_prebuilt)
        expected = [
            [0, 1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5, 6],
            [2, 3, 4, 3, 4, 5],
            [3, 4, 5, 4, 3, 4],
            [4, 5, 6, 5, 4, 3]
        ]
        self.assertEqual(result, expected)

class TestGetWordsWithMaxDistance(unittest.TestCase):
    def test_get(self):
        word_list = ["bat", "horse", "rat", "can", "ban", "cats"]
        word = "cat"
        result = get_words_with_max_distance(word, word_list, 1)
        expected = ["bat", "can", "cats", "rat"]
        self.assertEqual(set(result), set(expected))