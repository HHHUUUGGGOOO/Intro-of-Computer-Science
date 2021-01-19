#cipher

with open('/Users/user/Desktop/hw3/plain.txt', 'r', encoding='utf8') as f_str:
    f_str = f_str.read()
with open('/Users/user/Desktop/hw3/public_key.txt', 'r', encoding='utf8') as f_pkey:
    f_pkey = f_pkey.read()

#get "N,e"
count = 0
N = ''
e = ''
for i in range(len(f_pkey)):
    if f_pkey[i] == '\n':
        count += 1
        continue
    if count == 0:
        N += f_pkey[i]
    elif count == 1:
        e += f_pkey[i]
    elif count > 1:
        break
N, e = int(N), int(e)
        
#encode 
n = []
space = []
for i in range(int(len(f_str)/2+0.5)):
    temp = 0
    if f_str[2*i] == '':
        temp += ord(f_str[2*i+1])*2**8
        n.append(temp)
        space.append(2*i)
    elif f_str[2*i+1] == '':
        temp += ord(f_str[2*i])*2**8
        n.append(temp)
        space.append(2*i+1)
    else:
        temp = ord(f_str[2*i])*2**8 + ord(f_str[2*i+1])
        n.append(temp)

#encrypt
c = []
for i in range(len(n)):
    c.append(pow(n[i], e, N))
    
#output
with open('/Users/user/Desktop/hw3/secret.txt', 'w+', encoding='utf8') as f_sec:
    for i in range(len(c)):
        f_sec.write(str(c[i]))
        f_sec.write('\n')

		#decipher

with open('/Users/user/Desktop/hw3/secret.txt', 'r', encoding='utf8') as f_sec:
    f_sec = f_sec.read()
with open('/Users/user/Desktop/hw3/private_key.txt', 'r', encoding='utf8') as f_key:
    f_key = f_key.read()

#use some variable in cipher
with open('/Users/user/Desktop/hw3/plain.txt', 'r', encoding='utf8') as f_str:
    f_str = f_str.read()
n = []
space = []
for i in range(int(len(f_str)/2+0.5)):
    temp = 0
    if f_str[2*i] == '':
        temp += ord(f_str[2*i+1])*2**8
        n.append(temp)
        space.append(2*i)
    elif f_str[2*i+1] == '':
        temp += ord(f_str[2*i])*2**8
        n.append(temp)
        space.append(2*i+1)
    else:
        temp = ord(f_str[2*i])*2**8 + ord(f_str[2*i+1])
        n.append(temp)

#get "N,d"
count = 0
N_new = ''
d = ''
for i in range(len(f_key)):
    if f_key[i] == '\n':
        count += 1
        continue
    if count == 0:
        N_new += f_key[i]
    elif count == 1:
        d += f_key[i]
    elif count > 1:
        break
N_new, d = int(N_new), int(d)

#decrypt
c_new = []
temp = ''
count = 0
for i in range(len(f_sec)):
    if f_sec[i] == '\n':
        c_new.append(int(f_sec[(i-count):i]))
        temp = ''
        count = 0
    temp += f_sec[i]
    count += 1

n_new = []
for i in range(len(c_new)):
    n_new.append(pow(c_new[i], d, N_new))

#decode
m_new = []
count = 0
for i in range(len(n_new)):
    if count in space:
        m_new.append(' ')
    else:
        m_new.append(chr(n_new[i] // 256))
        count += 1
        m_new.append(chr(n_new[i] % 256))
        count += 1
mess = ''.join(m_new)    

#output
with open('/Users/user/Desktop/hw3/message.txt', 'w+', encoding='utf8') as f_mess:
    f_mess.write(mess)

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