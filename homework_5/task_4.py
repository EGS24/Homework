# Задача 4. Крестики нолики
# Напишите программу, которая реализует игру Крестики-нолики.
# Ваши классы в этой задаче могут выглядеть так:
# class Cell:
#  # Клетка, у которой есть значения
#  # - занята она или нет
#  # - номер клетки
# class Board:
#  # Класс поля, который создаёт у себя экземпляры клетки
# class Player:
#  # У игрока может быть
#  # - имя
#  # - на какую клетку ходит
class Cell:
    def __init__(self, number_of_cell):
        self.number_of_cell = number_of_cell
        self.busy_value = " "

    def is_empty_cell(self):  # проверка пуста ли клетка
        return self.busy_value == " "

    def set_value_symbol(self, symbol):  # установка символа
        if self.is_empty_cell():
            self.busy_value = symbol
            return True
        return False


class Board:
    def __init__(self):
        self.cells_board = [Cell(i) for i in range(1, 10)]

    def view_display(self):  # вывод доски
        print("━" * 13)
        for i in range(0, 9, 3):
            row = [self.cells_board[i].busy_value, self.cells_board[i + 1].busy_value,
                   self.cells_board[i + 2].busy_value]
            print(f"┃ {' ┃ '.join(row)} ┃")
            print("━" * 13)

    def is_full_board(self):  # проверка заполнена ли доска
        return all(not _.is_empty_cell() for _ in self.cells_board)

    def check_win_game(self, symbol):  # проверка на все варианты победы
        for i in range(0, 9, 3):
            if all(self.cells_board[i + j].busy_value == symbol for j in range(3)):  # строки
                return True
        for i in range(3):
            if all(self.cells_board[i + j * 3].busy_value == symbol for j in range(3)):  # столбцы
                return True
        if (self.cells_board[0].busy_value == symbol and self.cells_board[4].busy_value == symbol  # \
                and self.cells_board[8].busy_value == symbol):
            return True
        if (self.cells_board[2].busy_value == symbol and self.cells_board[4].busy_value == symbol  # /
                and self.cells_board[6].busy_value == symbol):
            return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board_display, number_cell):  # делаем ход
        if 1 <= number_cell <= 9:
            cell = board_display.cells_board[number_cell - 1]
            if cell.set_value_symbol(self.symbol):
                return True
        return False


if __name__ == "__main__":
    board = Board()
    player_1 = Player("Игрок 1", "X")
    player_2 = Player("Игрок 2", "O")
    current_player = player_1

    while True:
        board.view_display()  # выводим доску
        cell_number = int(
            input("\n{}, введите номер свободной клетки [1-9]: ".format(current_player.name))  # номер клетки
        )
        if current_player.make_move(board, cell_number):
            if board.check_win_game(current_player.symbol):  # проверяем на победу
                board.view_display()
                print("{} выиграл. Победа!".format(current_player.name))
                break
            elif board.is_full_board():  # проверяем, если доска заполнена, и никто не выиграл
                board.view_display()
                print("Ничейный счет.")
                break
            else:
                current_player = player_2 if current_player == player_1 else player_1  # смена хода
        else:
            print("Неправильный ход. Повторите попытку!")  # если неверно ввели
