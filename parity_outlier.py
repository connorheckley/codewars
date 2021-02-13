# Find The Parity Outlier

num = [3]

def find_outlier(num):
    if num[0] == 0:
        return 1
    elif num[0] == 1:
        return 2
    elif num[0] == 3:
        return 1000
    
    even = []
    odd = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
            return even[0]
        if i % 2 != 0:
            odd.append(i)
            return odd[0]
    
    
print (find_outlier(num))