# class TableError

class Table:
    """
    A table is a data structure storing a set of rows
    and the names of their elements. Each item in the list has a name -
    the name of the column.
    """
    __slots__ = ["rows"]

    def __init__(self, columns: list):
        """
        Args:
            columns: (list) A list of table columns names.
        """
        self.rows = [columns]

    def __str__(self):
        """Returns str: string format of Table  object"""
        return "<Table with {0}>".format(self.rows[0])

    def __repr__(self):
        """Returns str: string table representation"""
        repr_table = ""
        for row in self.rows:
            repr_table += " ".join([str(_) for _ in row])
            repr_table += "\n"
        return repr_table.rstrip()

    def __len__(self):
        """Returns int: the number of rows in the table"""
        return len(self.rows) - 1

    def __iter__(self):
        """
        Returns iterator:
        when calling next, a dictionary is returned
            keys are the names of the columns
            values are the corresponding values in the next row.

        >>> next(table)
        {'A': 1, 'B': 2, 'C': 3}
        """
        for el in self.rows[1:]:
            yield {k:v for k, v in zip(self.rows[0], el)}

    @property
    def next_index(self) -> int:
        """
        Returns int: the line number that will be assigned to the next line added.
        """
        return len(self.rows)

    def validate(self, row):
        """
        A method that verifies that a string matches requirements. 
        The only requirement here is matching sizes: 
        the row length must match the number of columns in the table.
        """
        if len(self.rows[0]) != len(row):
            raise TableError
        return row

    def add_row(self, row: list) -> int:
        """Add new row to the table.
        Args:
            row: list of values to add to the table.
        Returns:
            int: Index of the new row.
        Raises:
            TableError: If given row is not valid.
        """
        if self.validate(row):
            self.rows.append(row)
        return len(self.rows) - 1

    def get_row(self, index: int) -> list:
        """The method returns a string with the specified index. 
        Args:
            index: int number of required row in the table.
        Returns:
            int: Index of the new row.
            None if there is no row with given index.
        """
        if len(self.rows) - 1 > index:
            return self.rows[index+1]

    def remove_row(self, index: int):
        """
        The method removes the row with the specified index from the table.
        """
        if len(self.rows) - 1 > index:
            del self.rows[index+1]

class TableError(Exception):
        pass

def test():
    cols = ['A', 'B', 'C']
    t = Table(cols)
    t.add_row([1, 2, 3])
    assert repr(t) == 'A B C\n1 2 3'
    assert str(t) == "<Table with ['A', 'B', 'C']>"
    r = t.get_row(0)
    assert r == [1, 2, 3]

    t.add_row([4, 5, 6])
    assert list(t) == [{'A': 1, 'B': 2, 'C': 3}, {'A': 4, 'B': 5, 'C': 6}]
    assert len(t) == 2


if __name__ == "__main__":
    test()
