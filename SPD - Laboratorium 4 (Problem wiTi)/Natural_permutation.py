from Generator import RandomNumberGenerator
import copy

class Natural_permutation:
    def __init__(self, seed, n):  
        #Zrodlo losowania
        self.seed = seed
        #Liczba zadan
        self.n = n
        #Kolejnosc
        self.nr = []
        #Czasy wykonania
        self.p = []
        #Wspolczynniki kary
        self.w = []
        #Wspolczynniki kary
        self.w_copy = []
        #Zadany termin zakonczenia
        self.d = []
        #Zadany termin zakonczenia
        self.d_copy = []
        #Suma czasów wykonania
        self.A = 0
        #Czasy kolejnosc
        self.Pi = []
        #Czasy rozpoczęcia
        self.S = []
        #Czasy zakonczenia
        self.C = []
        #Czasy rozpoczęcia
        self.S_copy = []
        #Czasy zakonczenia
        self.C_copy = []
        #Czasy opóźnienia
        self.T = []
        #Kara
        self.WT = []
        #Czasy opóźnienia
        self.T_copy = []
        #Kara
        self.WT_copy = []
        #Ważona suma opóźnień wszystkich zadań
        self.SumWT = 0

        #Inicjalizacja obiektu
        rng = RandomNumberGenerator(seed)    

        #Inicjalizacja kolejnosci
        for i in range(1, n+1):
            self.nr.append(i);

        #Inicjalizacja czasow wykonania
        for i in range(0, n):
            random = rng.nextInt(1,29);
            self.p.append(random)
            self.A = self.A + random
            
        #Inicjalizacja wspolczynnikow kary 
        for i in range(0, n):
            self.w.append(rng.nextInt(1,9))

        #Inicjalizacja wspolczynnikow kary 
        for i in range(0, n):
            #self.d.append(rng.nextInt(1,self.A))
            self.d.append(rng.nextInt(1,29))

        for i in self.nr:
            self.Pi.append(i)

        self.CalculateS()
        self.CalculateC()
        self.CalculateT()
        self.CalculateWT()
        self.Sum()

    def CalculateS(self):
        self.S.clear()
        s = 0
        for i in self.Pi:
            self.S.append(s)
            s = s + self.p[i-1]

    def CalculateC(self):
        self.C.clear()
        s = 0
        for i in self.Pi:
            s = s + self.p[i-1]
            self.C.append(s)

    def CalculateT(self):
        self.T.clear()
        for i in range(0, self.n):
            self.T.append(max(self.C[i]-self.d[i],0))

    def CalculateWT(self):
        self.WT.clear()
        for i in range(0, self.n):
            self.WT.append(self.w[i]*self.T[i])

    def Sum(self):
        self.SumWT= 0
        for i in self.WT:
            self.SumWT = self.SumWT + i

    def CalculateSCustom(self, Pi):
        self.S_copy.clear()
        s = 0
        for i in Pi:
            self.S_copy.append(s)
            s = s + self.p[i-1]

    def CalculateCCustom(self, Pi):
        self.C_copy.clear()
        s = 0
        for i in Pi:
            s = s + self.p[i-1]
            self.C_copy.append(s)

    def CalculateTCustom(self, Pi):
        self.T_copy.clear()
        for i in range(0, self.n):
            self.T_copy.append(max(self.C_copy[i]-self.d[Pi[i]-1],0))

    def CalculateWTCustom(self, Pi):
        self.WT_copy.clear()
        for i in range(0, self.n):
            self.WT_copy.append(self.w[Pi[i]-1]*self.T_copy[i])

    def SumCustom(self):
        Sum= 0
        for i in self.WT_copy:
            Sum = Sum + i
        return Sum

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " nr: " + str(self.nr) + "\n" + str1 + "p: " + str(self.p) + "\n" + str1 + "w: " + str(self.w) + "\n" + str1 + "d: " + str(self.d) + "\n" + str1 + "Pi: " + str(self.Pi) + "\n" + str1 + "S: " + str(self.S)  + "\n" + str1 + "C: " + str(self.C)  + "\n" + str1 + "T: " + str(self.T)  + "\n" + str1 + "WT: " + str(self.WT)  + "\n" + str1 + "wiTi sum: " + str(self.SumWT) 



