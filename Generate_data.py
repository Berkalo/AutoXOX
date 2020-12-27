import numpy as np
import pandas as pd
data = []
import random
num_dat = 150000

def concater(status, p1_moves, p2_moves, legl_moves):
    p1_maxmoves = [0]*5
    p2_maxmoves = [0]*5
    legl_max_moves = [0]*4

    for x in range(len(p1_moves)):
        p1_maxmoves[x] = p1_moves[x]

    for x in range(len(p2_moves)):
        p2_maxmoves[x] = p2_moves[x]

    for x in range(len(legl_moves)):
        legl_max_moves[x] = legl_moves[x]

    p1_maxmoves.extend(p2_maxmoves)

    p1_maxmoves.extend(legl_max_moves)

    if status == [1, 0]:
        wm = int(len(p1_moves)) #the time p1 wons
        p1_maxmoves.append(wm)
        p1_maxmoves.append(1)

        return p1_maxmoves

    elif status == [0, 1]:
        wm = int(len(p2_moves)) #the time p1 wons
        p1_maxmoves.append(wm)
        p1_maxmoves.append(2)
        return p1_maxmoves
    else:
        p1_maxmoves.append(0)
        p1_maxmoves.append(0)
        return p1_maxmoves


for _ in range(num_dat):
    legl_moves = [a for a in range(1, 10)]
    #print(legl_moves)
    p1_moves_list = []
    p2_moves_list = []
    status = [0, 0]
    num_move = 0

    def who_won(status, p1_moves, p2_moves,legl_moves):
        if status == [1,0]:
            print("Player1 Won")
            print(" with moves")
            print(p1_moves)
            print("oppnents moves")
            print(p2_moves)
            print("empty spacees")
            print(legl_moves)
        elif status == [0,1]:
            print("Player2 Won")
            print(" with moves")
            print(p2_moves)
            print("oppnents moves")
            print(p1_moves)
            print("empty spacees")
            print(legl_moves)

        elif status == [0,0]:
            print("it's a tie!\n")
            print("p1_moves")
            print(p1_moves)
            print("p2_moves")
            print(p2_moves)

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

    def get_move(inp):
        return inp


    while True:
        #print(num_move)
        if num_move == 9:
            break

        p1_move_artif = random.choice(legl_moves)
        while True:
            p1_move = get_move(p1_move_artif)
            #print(p1_move)
            if p1_move in legl_moves:
                legl_moves.remove(p1_move)
                p1_moves_list.append(p1_move)
                break
            #print("it's an illegal move!!!")
        status = check_win(p1_moves_list, 1)
        if sum(status) != 0:
            break
        num_move += 1
        if num_move == 9:
            break

        p2_move_artif = random.choice(legl_moves)
        #print(p2_move_artif)
        while True:
            #print("player2")
            p2_move = get_move(p2_move_artif)
            if p2_move in legl_moves:
                legl_moves.remove(p2_move)
                p2_moves_list.append(p2_move)
                break
            #print("it's an illegal move!!!")
        num_move += 1

        status = check_win(p2_moves_list, 2)
        if num_move == 9:
            break

        if sum(status) != 0:
            break

    data.append(concater(status, p1_moves_list, p2_moves_list, legl_moves))
    #result = who_won(status,p1_moves_list,p2_moves_list,legl_moves)

arr = np.array(data)
unique_arr = np.unique(arr,axis=0)
df = pd.DataFrame(unique_arr)
df.to_csv("2000000_sampl_unique.csv")