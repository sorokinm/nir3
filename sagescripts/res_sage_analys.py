
dim = 5
br_name = "res_branch_number_" + str(dim) + ".txt"
int_br_name = "res_integral_br_num_" + str(dim) + ".txt"
br_num_file = open("rand_nonsingular_matrix_br5.txt56160", "r")

int_br_file = open("rand_nonsingular_matrix_int_br5.txt56160", "r")

#stat_4 = {"2:0": 0, "2:1": 0, "2:2": 0, "3:0": 0, "3:1": 0, "3:2": 0, "4:0": 0, "4:1": 0, "4:2" : 0}
stat_4 = {}
b_lines = br_num_file.readlines()
i_lines = int_br_file.readlines()

for i in range(len(b_lines)):
    key = b_lines[i].strip() + ":" + i_lines[i].strip()
    if key in stat_4:
        stat_4[key] += 1
    else:
        stat_4[key] = 1

for key, value in stat_4.items():
    print(key + " -> " + str(value))


