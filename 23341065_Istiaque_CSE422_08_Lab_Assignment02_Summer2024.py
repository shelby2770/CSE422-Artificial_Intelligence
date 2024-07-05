import random

input_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment02_InputFile_Summer2024.txt")
output_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment02_OutputFile_Summer2024.txt", "w")
n, t = map(int, input_file.readline().split())
courses = [input_file.readline()[:-1] for i in range(n)]


def fitness(s):
    overlap_penalty = 0
    for i in range(t):
        cnt = 0
        for j in range(n):
            cnt += (s[i * n + j] == '1')
        overlap_penalty += max(0, cnt - 1)

    consistency_penalty = 0
    for i in range(n):
        cnt = 0
        for j in range(t):
            cnt += (s[j * t + i] == '1')
        consistency_penalty += abs(cnt - 1)
    return -overlap_penalty - consistency_penalty


def selection():
    return population[random.randint(0, len(population) - 1)], population[random.randint(0, len(population) - 1)]


def crossover(parent1, parent2):
    return parent1[:len(parent1) // 2] + parent2[len(parent1) // 2:]


def mutate(s):
    id = random.randint(0, len(s) - 1)
    return s[:id] + random.choice("01") + s[id + 1:]


population = [''.join(random.choices("01", k=n * t)) for i in range(10)]
population.sort(key=lambda i: -fitness(i))

for i in range(10):
    if fitness(population[0]) == 0:
        break
    next_gen = []
    for j in range(10):
        parent1, parent2 = selection()
        child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
        next_gen.append(mutate(child1))
        next_gen.append(mutate(child2))
    next_gen.sort(key=lambda i: -fitness(i))
    population = next_gen
output_file.write(f"{population[0]}\n{fitness(population[0])}")

input_file.close()
output_file.close()