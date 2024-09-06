input_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment03_InputFile_Summer2024_task2.txt")
output_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment03_OutputFile_Summer2024_task2.txt", "w")
max_level = 3

score = [3, 6, 2, 3, 7, 1, 2, 0]


def alpha_beta_pruning(level, id, maximizer_turn, alpha, beta):
    if level == max_level:
        return max(score[id], score[id + 1])
    ret = (-1 if maximizer_turn else 1) * float("inf")
    for i in range(2):
        val = alpha_beta_pruning(level + 1, id + i * (pow(2, (max_level - level))), maximizer_turn ^ 1, alpha, beta)
        if maximizer_turn:
            ret = max(ret, val)
            alpha = max(alpha, val)
        else:
            ret = min(ret, val)
            beta = min(beta, val)
        if beta <= alpha:
            break
    return ret


def pacman_game(c):
    res = alpha_beta_pruning(1, 0, 1, -float("inf"), float("inf"))
    mx = max(score)
    magic = mx - c
    if magic > res:
        output_file.write(f"The new minimax value is {magic}. Pacman goes {"right" if score.index(mx) >= len(score) // 2 else "left"} and uses dark magic\n")
    else:
        output_file.write(f"The minimax value is {res}. Pacman does not use dark magic\n")


pacman_game(int(input_file.readline()))
input_file.close()
output_file.close()
