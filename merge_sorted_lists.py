import unittest

def merge_sorted_lists(sorted_list1, sorted_list2):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        sorted_list1: The first sorted list.
        sorted_list2: The second sorted list.

    Returns:
        A new sorted list containing all elements from sorted_list1 and sorted_list2.
    """
    merged_list = []
    i, j = 0, 0

    while i < len(sorted_list1) and j < len(sorted_list2):
        if sorted_list1[i] < sorted_list2[j]:
            merged_list.append(sorted_list1[i])
            i += 1
        else:
            merged_list.append(sorted_list2[j])
            j += 1

    merged_list.extend(sorted_list1[i:])
    merged_list.extend(sorted_list2[j:])

    return merged_list


class TestMergeSortedLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(merge_sorted_lists([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge_sorted_lists([], [4, 5, 6]), [4, 5, 6])

    def test_disjoint_lists(self):
        self.assertEqual(merge_sorted_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_overlapping_lists(self):
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_duplicate_values(self):
        self.assertEqual(merge_sorted_lists([1, 2, 2, 3], [2, 3, 3, 4]), [1, 2, 2, 2, 3, 3, 3, 4])

    def test_identical_lists(self):
        self.assertEqual(merge_sorted_lists([1, 2, 3], [1, 2, 3]), [1, 1, 2, 2, 3, 3]) # corrected

    def test_negative_numbers(self):
        self.assertEqual(merge_sorted_lists([-3, -1, 0], [-2, 1, 2]), [-3, -2, -1, 0, 1, 2])

    def test_mixed_numbers(self):
        self.assertEqual(merge_sorted_lists([-1, 0, 2], [-2, 1, 3]), [-2, -1, 0, 1, 2, 3])



if __name__ == '__main__':
    unittest.main()
