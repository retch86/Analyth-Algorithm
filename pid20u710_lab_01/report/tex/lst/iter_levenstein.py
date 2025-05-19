def iterative_levenstein_two_rows(str_1: str, str_2: str) -> int:
    len_str_1 = len(str_1); len_str_2 = len(str_2)
    flag_first_row = 1; flag_second_row = 2

    row_1 = create_row(len_str_1 + 1, flag_first_row)
    row_2 = create_row(len_str_1 + 1, flag_second_row)

    for i in range(1, len_str_2 + 1):
        row_2[0] = i
        for j in range(1, len_str_1 + 1):
            deletion_cost = row_1[j] + 1
            insert_cost = row_2[j - 1] + 1
            replace_cost = row_1[j - 1] if str_1[j - 1] == str_2[i - 1] 
                else row_1[j - 1] + 1

            row_2[j] = min(deletion_cost, insert_cost, replace_cost)
        row_1, row_2 = swap_rows(row_1, row_2)
    distance = row_1[-1]
    return distance