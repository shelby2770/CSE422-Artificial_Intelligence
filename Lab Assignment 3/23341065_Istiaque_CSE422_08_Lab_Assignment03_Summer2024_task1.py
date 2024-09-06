import random

input_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment03_InputFile_Summer2024_task1.txt")
output_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment03_OutputFile_Summer2024_task1.txt", "w")
turn = int(input_file.readline())
player = ["Scorpion", "Sub-Zero"]
cnt = [0, 0]
res = []
max_depth = 5


def alpha_beta_pruning(depth, maximizer_turn, alpha, beta):
    if depth == max_depth:
        return random.choice((1, -1))
    ret = (-1 if maximizer_turn else 1) * float("inf")
    for i in range(2):
        val = alpha_beta_pruning(depth + 1, maximizer_turn ^ 1, alpha, beta)
        if maximizer_turn:
            ret = max(ret, val)
            alpha = max(alpha, val)
        else:
            ret = min(ret, val)
            beta = min(beta, val)
        if beta <= alpha:
            break
    return ret


for i in range(3):
    if alpha_beta_pruning(0, turn, -float("inf"), float("inf")) == -1:
        cnt[0] += 1
        res.append(player[0])
    else:
        cnt[1] += 1
        res.append(player[1])
    turn ^= 1

output_file.write(f"Game Winner: {player[cnt[0] < cnt[1]]}\nTotal Rounds Played: 3\n")
for i in range(3):
    output_file.write(f"Winner of Round {i + 1}: {res[i]}\n")

input_file.close()
output_file.close()
