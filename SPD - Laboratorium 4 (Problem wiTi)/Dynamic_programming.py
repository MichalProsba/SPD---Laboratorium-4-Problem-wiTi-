from Natural_permutation import Natural_permutation
import math
import copy

class Dynamic_programming(Natural_permutation) : 
    def __init__ (self, seed, n):
        super().__init__(seed, n)
        self.D = []
        self.M = []
        self.T = []
        self.BT = []
        self.Trace = []

        for i in range(0,2**self.n):
            self.D.append(i)

        for i in range(0,2**self.n):
            self.M.append(-1)

    def Dynamic_programing(self):
        for i in self.D:
            p_sum = self.sum(i)
            self.M[i] = self.memoryD(p_sum, i)
        self.BackTracking()
        self.CalculateSCustom(self.Pi)
        self.CalculateCCustom(self.Pi)
        self.CalculateTCustom(self.Pi)
        self.CalculateWTCustom(self.Pi)
        self.S = copy.deepcopy(self.S_copy)
        self.C = copy.deepcopy(self.C_copy)
        self.T = copy.deepcopy(self.T_copy)
        self.WT = copy.deepcopy(self.WT_copy)
        self.Sum()
            
    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + "Pi: " + str(self.Pi) + "\n" + str1 + "S: " + str(self.S)  + "\n" + str1 + "C: " + str(self.C)  + "\n" + str1 + "T: " + str(self.T)  + "\n" + str1 + "WT: " + str(self.WT)  + "\n" + str1 + "wiTi sum: " + str(self.SumWT) 
    
    def sum(self, bit_number):
        p_sum = 0
        for i in range(0,self.n):
            check = 1 << i
            result = bit_number & check
            if(result == check):
                p_sum = p_sum + self.p[i]
        return p_sum

    def memoryD(self, p_sum, bit_number):
        min_index = 0
        min_value = 1000000
        if(bit_number == 0):
            min_value = 0
        max_value = 0
        binary_full = (2**self.n) - 1
        for i in range(0,self.n):
            check = 1 << i
            result = bit_number & check
            if(result == check):
                multiplyer = binary_full & (~(1 << i))
                before_indeks = bit_number & multiplyer 
                max_value = max((p_sum - self.d[i]),0)*self.w[i] + self.M[before_indeks]
                if(min_value > max_value):
                    min_value = max_value
                    min_index = before_indeks
        self.T.append(min_index)
        return min_value;

    def BackTracking(self):
        j = self.T[len(self.T)-1]
        for i in range(0,self.n):
            self.BT.append(j)
            j = self.T[j]
        for i in range(0,len(self.BT)-1):
            self.Trace.append(int(math.log((self.BT[len(self.BT)-i-2] - self.BT[len(self.BT)-i-1]),2)+1))
        for i in range(1,self.n+1):
            if not(i in self.Trace):
                self.Trace.append(i)
        self.Pi = list(self.Trace)
                
            
