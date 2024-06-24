import heapq

f = open("23341065_Istiaque_CSE422_08_Lab_Assignment01_InputFile_Summer2024.txt")

dict = {}
dict2 = {}
for i, j in enumerate(f):
    dict[j.split()[0]] = i
    dict2[i] = j.split()[0]
f.seek(0)

n = len(dict)
adj = [[] for i in range(n)]
h = [None for i in range(n)]

for i, j in enumerate(f):
    lst = j.split()
    h[i] = int(lst[1])
    for k in range(2, len(lst), 2):
        adj[i].append((dict[lst[k]], int(lst[k + 1])))

s = dict[input("Start node: ")]
d = dict[input("Destination: ")]
pq = []
vis = [float('inf') for i in range(n)]
par = [None for i in range(n)]
vis[s] = h[s]
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
    print("NO PATH FOUND")
else:
    path = [d]
    dist = 0
    now = d
    while par[now]:
        path.append(par[now][0])
        dist += par[now][1]
        now = par[now][0]
    print("Path: ", end='')
    for i in range(len(path) - 1, -1, -1):
        print(dict2[path[i]], end=" -> " if i else "\n")
    print("Total distance:", dist, "km")
