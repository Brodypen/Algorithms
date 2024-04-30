# The first line consists of 
#  space-separated integers, 
# , the number of tasks you need to do on the first day and the total number of tasks. The next 
#  lines each consist of 
#  integers 
#  and 
# , where 
# .

# Output
# Output “YES” if the run can be potentially successful, and “NO” otherwise.

def speedrun():
    n, m = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        set1 = set(range(a, b+1))
        if i == 0:
            set2 = set1
        else:
            set2 = set1.intersection(set2)
    print("YES")
