import random
from Student import Student

class Program:
    @staticmethod
    def main():
        students = [
            Student("Иван Иванов", "4", [random.uniform(2, 5) for _ in range(5)]),
            Student("Саша Петров", "4", [random.uniform(2, 5) for _ in range(5)]),
            Student("Кирилл Сидоров", "3", [random.uniform(2, 5) for _ in range(5)]),
            Student("Кузя Старков", "2", [random.uniform(2, 5) for _ in range(5)]),
            Student("Сергей Рид", "1", [random.uniform(2, 5) for _ in range(5)]),
            Student("Алексей Любин", "4", [random.uniform(2, 5) for _ in range(5)]),
            Student("Екатерина Мироненко", "4", [random.uniform(2, 5) for _ in range(5)]),
            Student("Елизавета Кузьмина", "4", [random.uniform(2, 5) for _ in range(5)]),
            Student("Анастасия Попова", "5", [random.uniform(2, 5) for _ in range(5)]),
            Student("Ксения Сидорова", "5", [random.uniform(2, 5) for _ in range(5)]),
        ]
        students = sorted(students, key=lambda student: student.get_average_grade())
        print("\n".join(map(str, students)))

if __name__ == '__main__':
    Program.main()