board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
legl_moves = [a for a in range(1, 10)]
p1_moves_list = []
p2_moves_list = []
max_count = 9
status = [0, 0]

def who_won(status):
    if status == [1,0]:
        print("Player1 Won")
    elif status == [0,1]:
        print("Player2 Won")
    elif status == [0,0]:
        print("it's a tie!")

def check_win(arr, player):  # player =1 || =2
    win_sit = [[1, 4, 7], [1, 5, 9], [1, 2, 3],
               [2, 5, 8], [3, 6, 9], [3, 5, 7],
               [4, 5, 6], [7, 8, 9]]
    status= [0, 0]  # 0th position for 1t players status, the 1th 2. player'ın durumu
    for x in win_sit:
        tmp_win = []
        for a in arr:
            if a in x:
                tmp_win.append(a)
        if len(tmp_win) == 3:
            status[player - 1] = 1
            return status
    return status

def get_move():
    return int(input())

def play():
    num_move = 0
    while True:
        print(num_move)
        if num_move == 9:
            break

        while True:
            print("player1 moves")
            p1_move = get_move()
            if p1_move in legl_moves:
                legl_moves.remove(p1_move)
                p1_moves_list.append(p1_move)
                break
            print("it's an illegal move!!!")
        status = check_win(p1_moves_list, 1)
        if sum(status) != 0:
            break
        num_move += 1
        if num_move == 9:
            break

        while True:
            print("player2")
            p2_move = get_move()
            if p2_move in legl_moves:
                legl_moves.remove(p2_move)
                p2_moves_list.append(p2_move)
                break
            print("it's an illegal move!!!")
        num_move += 1

        status = check_win(p2_moves_list, 2)
        if num_move == 9:
            break

        if sum(status) != 0:
            break

    return who_won(status)

play()