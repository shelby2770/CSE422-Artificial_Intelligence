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


def selection(n):
    return population[random.randint(0, n - 1)], population[random.randint(0, n - 1)]


def crossover(parent1, parent2):
    return parent1[:len(parent1) // 2] + parent2[len(parent1) // 2:]


def mutate(s):
    id = random.randint(0, len(s) - 1)
    return s[:id] + random.choice("01") + s[id + 1:]


population = [''.join(random.choices("01", k=n * t)) for i in range(10)]
tmp = population  # soterd initial population for later part
population.sort(key=lambda i: -fitness(i))

# part 1
for i in range(10):
    if fitness(population[0]) == 0:
        break
    next_gen = []
    for j in range(10):
        parent1, parent2 = selection(len(population))
        offspring1, offspring2 = crossover(parent1, parent2), crossover(parent2, parent1)
        next_gen.append(mutate(offspring1))
        next_gen.append(mutate(offspring2))
    next_gen.sort(key=lambda i: -fitness(i))
    population = next_gen
output_file.write(f"{population[0]}\n{fitness(population[0])}\n")


# part 2
def two_point_crossover(parent1, parent2):
    point1 = random.randint(1, len(parent1) - 2)
    point2 = random.randint(point1, len(parent1) - 1)
    return (parent1[:point1] + parent2[point1:point2] + parent1[point2:],
            parent2[:point1] + parent1[point1:point2] + parent2[point2:])


parent1, parent2 = random.choices(tmp, k=2)
offspring1, offspring2 = two_point_crossover(parent1, parent2)
output_file.write(f"Parent 1: {parent1}\nParent 2: {parent2}\nOffspring 1: {offspring1}\nOffspring 2: {offspring2}\n")

input_file.close()
output_file.close()
