import heapq
N, M = map(int, input().split())
l = list(map(lambda x:int(x)*(-1), input().split()))

# for i in range(M):
#     ind = l.index(max(l))
#     l[ind] = int(max(l) / 2)
#O(NM) = 10^10 で間に合わない

heapq.heapify(l)

for i in range(M):
    m = heapq.heappop(l)
    heapq.heappush(l, -1*(-m//2))
    
print(-sum(l))