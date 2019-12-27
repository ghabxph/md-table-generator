class TableCreator:
    """
    TableCreator class
    """

    def __init__(self, row, col, size):
        """
        Creates a TableCreator instance

        :param row:
        :param col:
        :param size:
        """

        self.row = row
        self.col = col
        self.size = size
        self.table = ""
        pass

    def create_table(self):
        """
        Creates table from given parameter

        :return self:
        """
        # The header part
        self.table = "|"
        for y in range(self.col):
            for z in range(self.size):
                self.table = self.table + " "
            self.table = self.table + "|"
        self.table = self.table + "\n"

        # The separator from header and regular data
        self.table = self.table + "|"
        for y in range(self.col):
            for z in range(self.size):
                self.table = self.table + "-"
            self.table = self.table + "|"
        self.table = self.table + "\n"

        # The data part (applies row)
        for x in range(self.row):
            self.table = self.table + "|"
            for y in range(self.col):
                for z in range(self.size):
                    self.table = self.table + " "
                self.table = self.table + "|"
            self.table = self.table + "\n"

        return self

    def to_string(self):
        """
        Returns the output table as markdown string

        :return:
        """
        return self.table
