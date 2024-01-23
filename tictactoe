class TicTacToe:
    def __init__(self):
        self.board = [[0, 0, 0] for _ in range(3)]
        self.mark = {1: "〇", -1: "×", 0: "　"}

    def input(self, player):
        while True:
            print("\n" + self.mark[player] + "の番")
            y, x = self.get_valid_input("行"), self.get_valid_input("列")
            if self.board[y][x] == 0:
                self.board[y][x] = player
                break
            print("既に埋まっているセルです")

    def get_valid_input(self, prompt):
        while True:
            try:
                val = int(input(prompt + "(0～2):"))
                if 0 <= val <= 2:
                    return val
                else:
                    print("0から2の間の数字を入力してください。")
            except ValueError:
                print("入力値が無効です！")

    def display(self):
        print("行列 0   1   2")
        for i in range(3):
            self.display_row(i)
            if i < 2:
                print("　　ー＋ー＋ー")

    def display_row(self, row):
        print(f"{row}   " + " | ".join(self.mark[self.board[row][i]] for i in range(3)))

    def compCheck(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False


def main():
    game = TicTacToe()
    player = 1

    for _ in range(9):
        game.display()
        game.input(player)

        if game.compCheck(player):
            game.display()
            print("■■" + game.mark[player] + "の勝ち！■■")
            break

        player *= -1
    else:  # This block executes if the loop was not broken (i.e., a draw)
        game.display()
        print("■■  引き分けです！　■■")

    input("終了します！")


if __name__ == "__main__":
    main()
