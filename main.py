from onehalfopt import *
from BNB import *
from dptsp import *
from genetic import *
from tspnaive import *
import time



#naive algo
print("\nNaive algorithm: \n\n")
start1 = time.process_time()
naive()
end1 = time.process_time()
print("\ntime taken for naive: ",end1 - start1)

#dp_algo
print("\nDynamic programming algorithm: \n\n")
start2 = time.process_time()
dp_algo() 
end2 = time.process_time()
print("time taken for Dynamic programming: ",end2 - start2)

#bound and branch algo
print("\nBranch and bound algorithm: \n\n")
start3 = time.process_time()
bnb() 
end3 = time.process_time()
print("\ntime taken for branch and bound : ",end3 - start3)


#1.5 opt algorithm
print("\n3/2 opt algorithm: \n\n")
start4 = time.process_time()
one_and_half_algo()
end4 = time.process_time()
print("time taken for 3/2 approximation algorithm: ",end4 - start4)


#genetic algorithm
print("\nGenetic algorithm: \n\n")
start5 = time.process_time()
genetic()
end5 = time.process_time()
print("time taken for  Genetic algorithm for 50 iterations: ",end5 - start5)
