# 0-1 knapsack 

def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapsack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1))

def main():
    num = int(input("Enter number of items: "))
    wt, val = [], []
    print("Enter weight and value of each item:")
    for i in range(num):
        w, v = map(int, input().split())
        wt.append(w)
        val.append(v)
    W = int(input("Enter the maximum weight: "))
    print(knapsack(W, wt, val, num))
    
if __name__ == "__main__":
    main()