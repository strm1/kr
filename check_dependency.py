def control(lst):
    if lst[0][0] != 0 and lst[1][1] == lst[0][0] and lst[2][2] == lst[0][0]: #Diagonal left to right
        '''print("debug1")''';return lst[1][1]
    elif lst[0][2] != 0 and lst[1][1] == lst[0][2] and lst[2][0] ==  lst[0][2] :#Diagonal right to left
        '''print("debug2")''';return lst[1][1]
    for i in range(3):
        if lst[0][i] != 0 and lst[1][i] == lst[0][i] and lst[2][i] ==  lst[0][i]:#Vertical for
            '''print("debug for 1")''';return lst[1][i]
        else: continue
    for i in range(3):
        if lst[i][0] != 0 and lst[i][1] == lst[i][0] and lst[i][2] ==  lst[i][0]:#Horizintal for
            '''print("debug for 2")''';return lst[i][1]
        else: continue
    if 0 not in lst[0] and 0 not in lst[1] and 0 not in lst[2]:
        return 0   #Nichja

    if __name__=="__main__":
        control(lst)
        