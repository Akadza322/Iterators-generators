class FlatIterator:

    def __init__(self, list_of_list):
        self.main_of_list = self.flatten(list_of_list)

    def flatten(self, lists):
        if lists == []:
            return lists
        if isinstance(lists[0], list):
            return self.flatten(lists[0]) + self.flatten(lists[1:])
        return lists[:1] + self.flatten(lists[1:])

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.main_of_list):
            raise StopIteration
        item = self.main_of_list[self.index]
        self.index += 1
        return item



def test_3():
    list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()