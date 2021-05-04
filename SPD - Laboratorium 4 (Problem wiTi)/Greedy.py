from Natural_permutation import Natural_permutation
import copy

class Greedy (Natural_permutation) : 
    def __init__ (self, seed, n):
        super().__init__(seed, n)

        #Sortujemy po czasie przygotowania, (zawsze pierwszy argument jest tym po ktorym sie sortuje), funkcja zip laczy elementy listy tak, że lista 10 elementowa staje sie tablica 3 na 10
        Sort_d, Sort_Pi, Sort_nr, Sort_w = zip(*[(x,y,z,w)for x, y, z, w in sorted(zip(self.d,self.Pi,self.nr, self.w))])
        self.w=list(Sort_w)
        self.d=list(Sort_d)
        self.Pi=list(Sort_Pi)
        self.nr=list(Sort_nr)

        self.CalculateS()
        self.CalculateC()
        self.CalculateT()
        self.CalculateWT()
        self.Sum()

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + "Pi: " + str(self.Pi) + "\n" + str1 + "S: " + str(self.S)  + "\n" + str1 + "C: " + str(self.C)  + "\n" + str1 + "T: " + str(self.T)  + "\n" + str1 + "WT: " + str(self.WT)  + "\n" + str1 + "wiTi sum: " + str(self.SumWT) 


