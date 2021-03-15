class TicTacGame:
    desk = list(range(1, 10))
    turn = True  # true - 1-st player, false - second player

    def show_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.desk[0 + i * 3], "|", self.desk[1 + i * 3], "|", self.desk[2 + i * 3], "|")
            print("-" * 13)

    def validate_input(self, ans):
        if ans == "stop":
            print("игра закончилась")
            exit(0)
        try:
            ans = int(ans)
        except:
            return False, 'Некорректный ввод. Введите число'
        if 1 <= ans <= 9:
            if ans == self.desk[ans - 1]:
                return True, ans
            else:
                return False, "Клетка занята, введите другое число"
        else:
            return False, "Введите число от 1 до 9"

    def start_game(self):
        a, b = self.check_winner()
        while not a:
            self.show_board()
            if self.turn:
                print("Ход игрока 1:")
            else:
                print("Ход игрока 2:")

            key, ans = self.validate_input(input())
            while not key:
                print(ans)
                key, ans = self.validate_input(input())
                # цикл, пока не введут правильное значение
            self.desk_input(ans)
            a, b = self.check_winner()
            self.turn = not self.turn  # смена хода

        self.show_board()  # последний показ доски и затем вывод победителя
        return b

    def desk_input(self, ans):
        if self.turn:
            self.desk[ans - 1] = "X"
            return self.desk
        else:
            self.desk[ans - 1] = "O"
            return self.desk

    def check_winner(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if "X" == self.desk[each[0]] == self.desk[each[1]] == self.desk[each[2]]:
                return True, "Победил игрок 1"
            if "O" == self.desk[each[0]] == self.desk[each[1]] == self.desk[each[2]]:
                return True, "Победил игрок 2"
        return False, "Победителя еще нет"


if __name__ == '__main__':
    game = TicTacGame()
    print(game.start_game())
