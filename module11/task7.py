from Matrix import Matrix

class Program:
    @staticmethod
    def main():
        first_matrix = Matrix(2, 3, [
            [1, 2, 3],
            [4, 5, 6]
        ])
        second_matrix = Matrix(2, 3, [
            [7, 8, 9],
            [10, 11, 12]
        ])
        print(first_matrix + second_matrix)
        print(second_matrix.transpose())

if __name__ == '__main__':
    Program.main()