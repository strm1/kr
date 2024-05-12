'''
 ---
|   |
'''

lst = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

def graphics(lst):
    str_ = " --- --- --- "
    for i in range(3):
        print(str_)
        full_str = ""
        for k in range(3):
            if lst[i][k] != 0:
                block = f"| {lst[i][k]} "
            elif lst[i][k] == 0:
                block = f"|   "
            full_str = full_str + block
        print(full_str + "|")
    print(str_)

if __name__=="__main__":
    graphics(lst)
    