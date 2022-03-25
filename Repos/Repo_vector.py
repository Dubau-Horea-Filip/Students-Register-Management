"""
The repository module
"""
import unittest


class Repository:

    def __init__(self, lst: list):
        self.repository = lst
        self.index = -1

    def __len__(self):
        return len(self.repository)

    def __delitem__(self, index):
        del self.repository[index]

    def add_item(self, item):
        self.repository.append(item)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        try:
            item = self.repository[self.index]
        except IndexError:
            self.index -= 1
            raise StopIteration()

        return item

    def __setitem__(self, index, value):
        self.repository[index] = value

    def __getitem__(self, index):
        return self.repository[index]

    @staticmethod
    def sort(the_list: list, function):
        """

        :param the_list:
        :param function:
        :return:
        """
        """
                for i in range(0, len(the_list)):
            for j in range(i + 1, len(the_list)):
                aux = function(the_list[i], the_list[j])
                if aux == the_list[j]:
                    the_list[i], the_list[j] = the_list[j], the_list[i]
        return the_list
        """
        # Start with a big gap, then reduce the gap
        n = len(the_list)
        gap = n // 2

        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped
        # order keep adding one more element until the entire array
        # is gap sorted
        while gap > 0:

            for i in range(gap, n):

                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = the_list[i]

                # shift earlier gap-sorted elements up until the correct
                # location for a[i] is found
                j = i
                while j >= gap and not function(the_list[j - gap], temp):
                    the_list[j] = the_list[j - gap]
                    j -= gap

                    # put temp (the original a[i]) in its correct location
                the_list[j] = temp
            gap //= 2

        return the_list

    @staticmethod
    def filter(the_list: list, function):
        """
        Filters a given list using an acceptance function given as a parameter
        :param the_list: The list to be filtered
        :param function: The acceptance function( witch returns true/false)
        :return: The filtered list
        """
        result = list()
        for item in the_list:
            if function(item):
                result.append(item)
        return result


class RepositoryTest(unittest.TestCase):

    def test_bas(self):
        a= Repository(list())
        b= 156
        a.add_item(b)
        a.add_item("ana")
        a.add_item("ben")
        a.add_item("jon")
        a.add_item("andy")
        c = len(a)
        self.assertEqual(5,c)


        list_iterator = iter(a)
        while True:
            try:
                d = next(list_iterator)
            except StopIteration:
                break

        del a[1]
        e= a[2]
        a[2]="ana"




    def test_filter(self):
        array = [1, 5, 10, 2, 7, 4, 3, 7, 200, 250, 45]
        expected = [5, 10, 200, 250, 45]
        self.assertEqual(Repository.filter(array, function=lambda x: x % 5 == 0), expected)
        expected = [5, 10, 200, 250, 45, 2]
        self.assertNotEqual(Repository.filter(array, function=lambda x: x % 5 == 0), expected)

    def test_sorted(self):
        array = [5, 1, 10, 2, 7, 4, 3, 7, 200, 250, 45]
        expected = [1, 2, 3, 4, 5, 7, 7, 10, 45, 200, 250]
        self.assertEqual(expected, Repository.sort(array, self.sort_integers))
        array = ["12345", "1234", "1", "12"]
        expected = ["1", "12", "1234", "12345"]
        self.assertEqual(expected, Repository.sort(array, self.sort_strings))

    def sort_integers(self, x, y):
        if x < y:
            return True
        else:
            return False

    def sort_strings(self, x, y):
        if len(x) < len(y):
            return True
        else:
            return False
