
list_a = [1,2,3,4,5,8,9,10,11,12,15,16,17,18,19]
list_b = [6,7,13,14,20,21]
list_c = []

cnt_limit = len(list_a) + len(list_b)
#print(cnt_limit)
count = 0
n = 0
x = 0
for i in range(cnt_limit):    

    if count <= 4:        
        list_c.append(list_a[x])
        x += 1
    
    if count > 4:        
        list_c.append(list_b[n])
        n += 1
    
    if count >= 6:
        print("count reset")
        print(list_c)
        count = 0
    else: count += 1    
    

print(list_c)  

    
