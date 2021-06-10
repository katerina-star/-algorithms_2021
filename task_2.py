"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if self.left_child == None:
            if self.left_child is None:
                if new_node >= self.get_root_val():
                    raise ValueError('Левый потомок должен быть меньше родительского узла!')
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                if new_node >= self.get_root_val() or new_node < self.get_left_child().get_root_val():
                    print('Значение родительского узла:', self.get_root_val())
                    raise ValueError('Левый потомок должен быть меньше родительского узла!')
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            if self.right_child is None:
                if new_node < self.get_root_val():
                    raise ValueError('Правый потомок должен быть больше родительского узла или равен ему!')
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                if new_node < self.get_root_val() or new_node > self.get_right_child().get_root_val():
                    print('Значение родительского узла:', self.get_root_val())
                    raise ValueError('Правый потомок должен быть больше родительского узла или равен ему!')
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

