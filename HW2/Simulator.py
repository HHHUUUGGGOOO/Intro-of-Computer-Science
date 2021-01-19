class Simulator:
    def __init__(self):
        self.memory = list()
        self.reg = [0]*16
        
    def loadMemory(self, path):
        with open(path, 'rb') as fin:
            memory = list(fin.read())
        self.memory = memory
    
    def storeMemory(self, path):
        with open(path, 'wb') as fout:
            for i in range(len(self.memory)):
                self.memory[i] = bytes([self.memory[i]])
            fout.write(b''.join(self.memory))

    def simulate(self):
        self.pc = 0
        new = 0
        while True:
            self.opcode = self.memory[self.pc]//16
        #1 RXY LOAD the register R with the bit pattern found in the memory
           #cell whose address is XY.
           #Example: 14A3 would cause the contents of the memory cell
           #located at address A3 to be placed in register 4.
            if self.opcode == 1:
                self.reg[self.memory[self.pc]%16] = self.memory[self.memory[self.pc+1]]

        #2 RXY LOAD the register R with the bit pattern XY.
           #Example: 20A3 would cause the value A3 to be placed in
           #register 0.            
            elif self.opcode == 2:
                self.reg[self.memory[self.pc]%16] = self.memory[self.pc+1]

        #3 RXY STORE the bit pattern found in register R in the memory cell
           #whose address is XY.
           #Example: 35B1 would cause the contents of register 5 to be
           #placed in the memory cell whose address is B1.
            elif self.opcode == 3:
                self.memory[self.memory[self.pc+1]] = self.reg[self.memory[self.pc]%16]
                
        #4 0RS MOVE the bit pattern found in register R to register S.
           #Example: 40A4 would cause the contents of register A to be
           #copied into register 4.
            elif self.opcode == 4:
                self.reg[self.memory[self.pc+1]%16] = self.reg[self.memory[self.pc+1]//16]

        #5 RST ADD the bit patterns in registers S and T as though they were
           #two’s complement representations and leave the result in register R.
           #Example: 5726 would cause the binary values in registers 2 and
           #6 to be added and the sum placed in register 7.
            elif self.opcode == 5:
                self.reg[self.memory[self.pc]%16] = (self.reg[self.memory[self.pc+1]//16] + self.reg[self.memory[self.pc+1]%16])%256

        #6 RST ADD the bit patterns in registers S and T as though they
           #represented values in floating-point notation and leave the
           #floating-point result in register R.
           #Example: 634E would cause the values in registers 4 and E to
           #be added as floating-point values and the result to be placed in
           #register 3.
            elif self.opcode == 6:
                final = 0
                temp_1 = bin(self.reg[self.memory[self.pc+1]//16])[2:].rjust(8, '0')   #load the value to the binary form
                temp_2 = bin(self.reg[self.memory[self.pc+1]%16])[2:].rjust(8, '0')
                temp_3 = ''
                expo = {'000':-4 , '001':-3 , '010':-2 , '011':-1 , '100':0 , '101':1 , '110':2 , '111':3}   #set some dictionaries
                exp_1 = {-4:'000' , -3:'001' , -2:'010' , -1:'011' , 0:'100' , 1:'101' , 2:'110' , 3:'111'}
                add_1 = (eval(temp_1[4])/2 + eval(temp_1[5])/4 + eval(temp_1[6])/8 + eval(temp_1[7])/16)*2**(expo[temp_1[1:4]])   #transfer the binaries to decimal and add them
                add_2 = (eval(temp_2[4])/2 + eval(temp_2[5])/4 + eval(temp_2[6])/8 + eval(temp_2[7])/16)*2**(expo[temp_2[1:4]])
                if temp_1[0] == '1':   #watch tje sign bit
                    add_1 *= (-1)
                if temp_2[0] == '1':
                    add_2 *= (-1)
                ans = add_1 + add_2
                if ans < 0:    #observe whether the sum is positive or negative or even zero
                    temp_3 += '1'
                elif ans == 0:
                    temp_3 += '01000000'
                elif ans > 0:
                    temp_3 += '0'
                if ans != 0 and (ans-int(ans)) != 0:   #change the floating points back to the binary form
                    ans = abs(ans)
                    ans_int = bin(int(ans))[2:]
                    t_1 = (ans-int(ans))*2
                    a_1 = int(t_1)
                    t_2 = (t_1-a_1)*2
                    a_2 = int(t_2)
                    t_3 = (t_2-a_2)*2
                    a_3 = int(t_3)
                    t_4 = (t_3-a_3)*2
                    a_4 = int(t_4)
                    mantissa = ans_int + str(a_1) + str(a_2) + str(a_3) + str(a_4)
                    if ans_int == '0':
                        man = str(a_1) + str(a_2) + str(a_3) + str(a_4)
                        zeros = 0
                        for i in range(4):
                            if man[i] == '0':
                                zeros += 1
                            else:
                                man = man[i:].ljust(4, '0')
                                break
                        temp_3 = temp_3 + exp_1[-zeros] + man
                    elif ans_int != '0':
                        man = mantissa[0:4]
                        temp_3 = temp_3 + exp_1[len(ans_int)] + man
                    for i in range(8):
                        final += eval(temp_3[i])*2**(7-i)
                    self.reg[self.memory[self.pc]%16] = final
                elif ans != 0 and (ans-int(ans)) == 0:   #change the decimals to the binary form
                    ans = abs(ans)
                    ans_int = bin(int(ans))[2:]
                    temp_3 = temp_3 + exp_1[len(ans_int)] + ans_int.ljust(4, '0')
                    for i in range(8):    
                        final += eval(temp_3[i])*2**(7-i)    #transfer the 8-bits data to decimal
                    self.reg[self.memory[self.pc]%16] = final
        #7 RST OR the bit patterns in registers S and T and place the result in
           #register R.
           #Example: 7CB4 would cause the result of ORing the contents of
           #registers B and 4 to be placed in register C.
            elif self.opcode == 7:
                self.reg[self.memory[self.pc]%16] = self.reg[self.memory[self.pc+1]//16] | self.reg[self.memory[self.pc+1]%16]

        #8 RST AND the bit patterns in registers S and T and place the result in
           #register R.
           #Example: 8045 would cause the result of ANDing the contents of
           #registers 4 and 5 to be placed in register 0.
            elif self.opcode == 8:
                self.reg[self.memory[self.pc]%16] = self.reg[self.memory[self.pc+1]//16] & self.reg[self.memory[self.pc+1]%16]

        #9 RST EXCLUSIVE OR the bit patterns in registers S and T and place
           #the result in register R.
           #Example: 95F3 would cause the result of EXCLUSIVE ORing the
           #contents of registers F and 3 to be placed in register 5.
            elif self.opcode == 9:
                self.reg[self.memory[self.pc]%16] = self.reg[self.memory[self.pc+1]//16] ^ self.reg[self.memory[self.pc+1]%16]

        #A R0X ROTATE the bit pattern in register R one bit to the right X times.
           #Each time place the bit that started at the low-order end at the
           #high-order end.
           #Example: A403 would cause the contents of register 4 to be
           #rotated 3 bits to the right in a circular fashion.
            elif self.opcode == 10:
                temp = bin(self.reg[self.memory[self.pc]%16])[2:].rjust(8, '0')
                rotate = temp*3
                step = self.memory[self.pc+1]%16
                ans = rotate[8-step:16-step]
                op_10 = 0
                for i in range(len(ans)):
                    op_10 += eval(ans[i])*2**(7-i)
                self.reg[self.memory[self.pc]%16] = op_10

        #B RXY JUMP to the instruction located in the memory cell at address
           #XY if the bit pattern in register R is equal to the bit pattern
           #in register number 0. Otherwise, continue with the normal
           #sequence of execution. (The jump is implemented by copying
           #XY into the program counter during the execute phase.)
           #Example: B43C would first compare the contents of register 4
           #with the contents of register 0. If the two were equal, the pattern
           #3C would be placed in the program counter so that the next
           #instruction executed would be the one located at that memory
           #address. Otherwise, nothing would be done and program
           #execution would continue in its normal sequence.
            elif self.opcode == 11:
                if self.reg[self.memory[self.pc]%16] == self.reg[0]:
                    new = self.memory[self.pc+1]
                else:
                    pass
        #C 000 HALT execution.
           #Example: C000 would cause program execution to stop.
            elif self.opcode == 12:
                break
            if self.pc == new:
                self.pc += 2
                new += 2
            else:
                self.pc = new

