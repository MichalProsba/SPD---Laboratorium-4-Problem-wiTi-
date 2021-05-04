from Generator import RandomNumberGenerator
from Natural_permutation import Natural_permutation
from Greedy import Greedy
from Brute_force import Brute_force
from Dynamic_programming import Dynamic_programming

seed = 6546
tasks = 8

str1 = "===================================================================\n"
print (str1 + "NATURAL PERMUTATION")
natural_permutation = Natural_permutation(seed, tasks)
print(natural_permutation)
print (str1 + "GREEDY")
greedy = Greedy(seed, tasks)
print(greedy)
print (str1 + "BRUTE FORCE")
brut = Brute_force(seed, tasks)
brut.First_Brute_force()
print(brut)
print (str1 + "DYNAMIC PROGRAMMING")
dynamic_programming = Dynamic_programming(seed, tasks)
dynamic_programming.Dynamic_programing()
print(dynamic_programming)