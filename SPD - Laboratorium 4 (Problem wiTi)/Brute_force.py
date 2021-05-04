from Natural_permutation import Natural_permutation
import copy

class Brute_force(Natural_permutation) : 
    def __init__ (self, seed, n):
        super().__init__(seed, n)
        self.allPi = []

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + "Pi: " + str(self.Pi) + "\n" + str1 + "S: " + str(self.S)  + "\n" + str1 + "C: " + str(self.C)  + "\n" + str1 + "T: " + str(self.T)  + "\n" + str1 + "WT: " + str(self.WT)  + "\n" + str1 + "wiTi sum: " + str(self.SumWT) 

    def First_Brute_force(self):
        Pi = []
        for i in range(0, self.n):
            self.Brute_force(copy.deepcopy(i), copy.deepcopy(Pi), copy.deepcopy(self.nr))
        self.Calculate()

    def Brute_force(self, j_star, Pi, Nr):
        Pi.append(Nr[j_star])
        del Nr[j_star]
        if len(Nr) > 0:
            for j in range(0, len(Nr)):
                self.Brute_force(copy.deepcopy(j), copy.deepcopy(Pi), copy.deepcopy(Nr))
        else:
            self.CalculateSCustom(Pi)
            self.CalculateCCustom(Pi)
            self.CalculateTCustom(Pi)
            self.CalculateWTCustom(Pi)
            Fmax = self.SumCustom()
            if Fmax < self.SumWT:
                self.SumWT = copy.deepcopy(Fmax)
                self.Pi = copy.deepcopy(Pi)

    def Calculate(self):
            self.CalculateSCustom(self.Pi)
            self.CalculateCCustom(self.Pi)
            self.CalculateTCustom(self.Pi)
            self.CalculateWTCustom(self.Pi)
            self.S = copy.deepcopy(self.S_copy)
            self.C = copy.deepcopy(self.C_copy)
            self.T = copy.deepcopy(self.T_copy)
            self.WT = copy.deepcopy(self.WT_copy)
            self.Sum()