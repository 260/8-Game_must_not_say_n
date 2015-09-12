#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/26

first_line = input()
game_times = int(first_line)

for game in range(game_times):
    line = input()
    max_num_and_given_num = list(map(int, line.split(' ')))
    max_num     = max_num_and_given_num[0]
    given_num   = max_num_and_given_num[1]
    if (max_num - 1) % (given_num + 1) == 0:
        print('Lose')
    else:
        print('Win')
