import random

input_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment02_InputFile_Summer2024.txt")
output_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment02_OutputFile_Summer2024.txt", "w")

n, t = map(int, input_file.readline().split())
courses = [input_file.readline()[:-1] for i in range(n)]
population = [''.join(random.choices("01", k=n * t)) for i in range(10)]


def fitness(s):
    overlap_penalty = 0
    for i in range(t):
        cnt = 0
        for j in range(n):
            cnt += (s[i * n + j] == '1')
        overlap_penalty += max(0, cnt - 1)

    consistency_penalty=0
    for i in range(n):
        cnt=0
        for j in range(t):
            cnt+= (s[j*t+i]=='1')
        consistency_penalty= abs(cnt-1)
    return -overlap_penalty-consistency_penalty

# for i in range(10):

input_file.close()
output_file.close()
