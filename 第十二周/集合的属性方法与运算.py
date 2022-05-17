if __name__ == '__main__':
    n = int(input())
    mySet = set()
    for _ in range(n+1):
        command = input().split()
        if command[0] == 'add':
            mySet.add(command[1])
        elif command[0] == 'print':
            print(sorted(mySet))
        elif command[0] == 'del':
            mySet.discard(command[1])
        elif command[0] == 'update':
            mySet.update(command[1:])
        elif command[0] == 'clear':
            mySet.clear()