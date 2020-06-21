from onehalfopt import *
from BNB import *
from dptsp import *
from genetic import *
from tspnaive import *
import time



#naive algo
print("\nNaive algorithm: \n\n")
start = time.process_time()
bnb() 
end = time.process_time()
print("\ntime taken for naive: ",end - start)

#dp_algo
print("\nDynamic programming algorithm: \n\n")
start = time.process_time()
dp_algo() 
end = time.process_time()
print("time taken for Dynamic programming: ",end - start)

#bound and branch algo
print("\nBound and branch algorithm: \n\n")
start = time.process_time()
bnb() 
end = time.process_time()
print("\ntime taken for bound and branch: ",end - start)


#1.5 opt algorithm
print("\n3/2 opt algorithm: \n\n")
start = time.process_time()
one_and_half_algo()
end = time.process_time()
print("time taken for 3/2 approximation algorithm: ",end - start)


#genetic algorithm
print("\nGenetic algorithm: \n\n")
start = time.process_time()
genetic()
end = time.process_time()
print("time taken for  Genetic algorithm for 50 iterations: ",end - start)
print("time taken for  Genetic algorithm for 1 iteration on avearge: ",(end - start)/50)