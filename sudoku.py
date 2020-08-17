class Sudoku:

    @staticmethod
    def check_data_part(data_part, number, pool_type):
        if set(data_part) != set(range(1, 10)):
            raise RuntimeError(f"{pool_type.capitalize()} {number} is invalid: {data_part}")

    @classmethod
    def check(cls, data):
        for i in range(9):
            cls.check_row(data, i)
            cls.check_column(data, i)
            cls.check_quadrant(data, i)

    @classmethod
    def check_quadrant(cls, data, quad_num):
        parts = [data[quad_num // 3 * 18 + quad_num * 3 + j * 9:quad_num // 3 * 18 + j * 9 + (quad_num + 1) * 3] for j in range(3)]
        cls.check_data_part(parts[0] + parts[1] + parts[2], quad_num, "quadrant")

    @classmethod
    def check_column(cls, data, col_num):
        column = [data[col_num + j * 9] for j in range(9)]
        cls.check_data_part(column, col_num, "column")

    @classmethod
    def check_row(cls, data, row_num):
        row = data[row_num * 9:(row_num + 1) * 9]
        cls.check_data_part(row, row_num, "row")


invalid_data = [5, 8, 9, 3, 1, 2, 4, 6, 7,
                7, 6, 1, 4, 9, 8, 2, 3, 5,
                2, 3, 4, 5, 7, 6, 0, 9, 8,
                3, 7, 8, 2, 4, 9, 9, 5, 6,
                4, 5, 2, 6, 8, 9, 3, 7, 1,
                1, 9, 6, 7, 3, 5, 8, 4, 2,
                6, 4, 5, 8, 2, 3, 7, 1, 9,
                9, 2, 3, 1, 5, 7, 6, 8, 4,
                8, 1, 7, 9, 6, 4, 5, 2, 5]

Sudoku.check(invalid_data)