# -*- coding: utf-8 -*-
import re
original_text = '../Data/original_follower.txt'
trimed_text = '../Data/trimed_follower.txt'

def correctOrder(c, line_origin):
    content = line_origin
    pattern = ".*さんのプロフィール写真"
    result = re.match(pattern, content)
    if result:
        return 1
    else:
        return c



def trimTextData():
    process_num = 0
    current_row_number_each_user = 0
    each_user_limit = 3
    trimed_string = ''
    with open(original_text, "r") as f_origin:
        for line_origin in f_origin:
            process_num += 1
            current_row_number_each_user += 1
            current_row_number_each_user = correctOrder(current_row_number_each_user, line_origin)

            if current_row_number_each_user == 1:
                #print(str(process_num) + "行目処理中 . . . \n\n")
                1
            elif current_row_number_each_user == 2:
                trimed_string += line_origin
            elif current_row_number_each_user == each_user_limit:
                current_row_number_each_user = 0
            else:
                print('エラーが発生しました。')

        with open(trimed_text, mode='w') as f_trimed:
            f_trimed.write(trimed_string)
        return

def main():
    trimTextData()

main()
