import unittest

a = [1, 7, 3, 25, 12, 9]


def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a) / 2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


class TestSort(unittest.TestCase):

    def test1(self):
        b = [5, 10, 67, 7, 3, 9]
        c = sorted(b)
        self.assertEqual(merge_sort(b), c)

    def test2(self):
        b = [3, 6, 2, 17, 29, 12]
        c = sorted(b)
        self.assertEqual(merge_sort(b), c)

    def test3(self):
        b = [18, 56, 157, 56, 34, 89]
        c = sorted(b)
        self.assertEqual(merge_sort(b), c)


if __name__ == '__main__':
    unittest.main()
