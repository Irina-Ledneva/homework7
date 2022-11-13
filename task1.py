class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        for row in self.lists:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.lists)):
            for j in range(len(other.lists[i])):
                self.lists[i][j] = self.lists[i][j] + other.lists[i][j]
        return Matrix.__str__(self)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a)
print(b)
print('Сумма матриц: ')
print(a + b)

