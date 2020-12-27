class play():
    legl_moves = [a for a in range(1, 10)]
    p_moves_list = []
    def __init__(self):
        self.status = [0, 0]
        self.num_move = 0

    def check_win(self, arr, player):  # player =1 || =2
        win_sit = [[1, 4, 7], [1, 5, 9], [1, 2, 3],
                   [2, 5, 8], [3, 6, 9], [3, 5, 7],
                   [4, 5, 6], [7, 8, 9]]
        status = [0, 0]  # 0th position for 1t players status, the 1th 2. player'ın durumu

        for x in win_sit:
            tmp_win = []
            for a in arr:
                if a in x:
                    tmp_win.append(a)
            if len(tmp_win) == 3:
                status[player - 1] = 1
                return status
        return status

    def get_move(self, a):
        return a

    def makes_move(self):
            p1_move = self.get_move(int(input()))
            if p1_move in play.legl_moves:
                play.legl_moves.remove(p1_move)
                play.p_moves_list.append(p1_move)
    print("it's an illegal move!!!")


