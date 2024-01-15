from Math import MyMath

class Program:
    @staticmethod
    def main():
        res1 = MyMath.circle_len(radius=5)
        res2 = MyMath.circle_sq(radius=6)
        print(res1)
        print(res2)

if __name__ == '__main__':
    Program.main()