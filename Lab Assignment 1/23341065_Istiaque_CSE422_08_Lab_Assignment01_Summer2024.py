import heapq

input_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment01_InputFile_Summer2024.txt")
output_file = open("23341065_Istiaque_CSE422_08_Lab_Assignment01_OutputFile_Summer2024.txt", "w")
adj = {}
h = {}

for i in input_file:
    lst = i.split()
    now = lst[0]
    h[now] = int(lst[1])
    adj[now] = []
    for k in range(2, len(lst), 2):
        adj[now].append((lst[k], int(lst[k + 1])))

s = input("Start node: ")
d = input("Destination: ")
vis = {key: float('inf') for key in adj.keys()}
par = {key: None for key in adj.keys()}
vis[s] = h[s]
pq = []
heapq.heappush(pq, (h[s], s))
while len(pq):
    val, now = heapq.heappop(pq)
    if vis[now] != val: continue
    if now == d: break
    val -= h[now]
    for i in adj[now]:
        if val + i[1] + h[i[0]] < vis[i[0]]:
            vis[i[0]] = val + i[1] + h[i[0]]
            par[i[0]] = (now, i[1])
            heapq.heappush(pq, (vis[i[0]], i[0]))

if vis[d] == float('inf'):
    output_file.write("NO PATH FOUND\n")
else:
    path = [d]
    dist = 0
    now = d
    while par[now]:
        path.append(par[now][0])
        dist += par[now][1]
        now = par[now][0]
    output_file.write("Path: ")
    for i in range(len(path) - 1, -1, -1):
        output_file.write(f"{path[i]}{" -> " if i else "\n"}")
    output_file.write(f"Total distance: {dist} km")

input_file.close()
output_file.close()
