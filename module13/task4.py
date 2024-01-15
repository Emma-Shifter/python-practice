from List import *

class Program:
    @staticmethod
    def main():
        linkedList = LinkedList()
        linkedList.append(1)
        linkedList.append(2)
        linkedList.append(3)
        print([i.get_item() for i in linkedList])
        print(linkedList.get(0).get_item())
        print(linkedList.get(1).get_item())
        print(linkedList.get(2).get_item())
        linkedList.remove(0)
        print([i.get_item() for i in linkedList])
        linkedList.remove(1)
        print(linkedList.get(0).get_item())
        print([i.get_item() for i in linkedList])

if __name__ == '__main__':
    Program.main()