import unittest
from main import TicTacGame


class InputTest(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()
        self.game.desk = list(range(1, 10))

    def test_validate_input(self):
        self.assertEqual(self.game.validate_input(5), (True, 5))
        self.assertEqual(self.game.validate_input(3), (True, 3))
        self.assertEqual(self.game.validate_input(7), (True, 7))

        self.assertEqual(self.game.validate_input(10), (False, "Введите число от 1 до 9"))
        self.assertEqual(self.game.validate_input(0), (False, "Введите число от 1 до 9"))

        self.assertEqual(self.game.validate_input("y"), (False, "Некорректный ввод. Введите число"))
        self.assertEqual(self.game.validate_input("k"), (False, "Некорректный ввод. Введите число"))
        self.assertEqual(self.game.validate_input(""), (False, "Некорректный ввод. Введите число"))
        self.assertEqual(self.game.validate_input(" "), (False, "Некорректный ввод. Введите число"))

        self.game.desk[0] = "O"
        self.game.desk[1] = "X"
        self.game.desk[2] = "X"
        self.assertEqual(self.game.validate_input(1), (False, "Клетка занята, введите другое число"))
        self.assertEqual(self.game.validate_input(2), (False, "Клетка занята, введите другое число"))
        self.assertEqual(self.game.validate_input(3), (False, "Клетка занята, введите другое число"))

    def test_show_board(self):
        self.assertEqual(self.game.desk, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_check_winner(self):
        a = self.game.desk
        self.assertEqual(self.game.check_winner(), (False, 'Победителя еще нет'))
        a[0] = 'X'
        a[1] = 'X'
        a[2] = 'X'
        self.assertEqual(self.game.check_winner(), (True, 'Победил игрок 1'))
        a[2] = 'O'
        a[5] = 'O'
        a[8] = 'O'
        self.assertEqual(self.game.check_winner(), (True, 'Победил игрок 2'))

    def test_desk_input(self):
        self.game.turn = True
        self.game.desk_input(1)
        self.game.desk_input(2)
        self.game.turn = False
        self.game.desk_input(3)
        self.game.desk_input(4)
        self.game.turn = True
        self.game.desk_input(5)
        self.game.desk_input(6)
        self.assertEqual(self.game.desk, ["X", "X", "O", "O", "X", "X", 7, 8, 9])


if __name__ == '__main__':
    unittest.main()

