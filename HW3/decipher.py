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
