#find
with open('/Users/user/Desktop/hw3/cryptan.txt', 'r', encoding='utf8') as f_cry:
    f_cry = f_cry.read()
    
#get "e,phi"
count = 0
e = ''
phi = ''
for i in range(len(f_cry)):
    if f_cry[i] == '\n':
        count += 1
        continue
    if count == 0:
        e += f_cry[i]
    elif count == 1:
        phi += f_cry[i]
    elif count > 1:
        break
e, phi = int(e), int(phi)

#find d_prime
k = 1
while True:
    d_prime = (phi*k + 1) % 3
    if d_prime != 0:
        k += 1
    else:
        d_prime = (phi*k + 1) // 3 
        break

#output
with open('/Users/user/Desktop/hw3/cryptan_result.txt', 'w+', encoding='utf8') as f_res:
    f_res.write(str(d_prime))
