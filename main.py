from onehalfopt import *
from BNB import *
from dptsp import *
from genetic import *
import time


#dp_algo
print("\nDynamic programming algorithm: \n\n")
start = time.process_time()
dp_algo() 
end = time.process_time()
print("time taken for bound and branch: ",end - start)

#bound and branch algo
print("\nbound and branch algorithm: \n\n")
start = time.process_time()
bnb() 
end = time.process_time()
print("\ntime taken for bound and branch: ",end - start)


#1.5 opt algorithm
print("\n1.5 opt algorithm: \n\n")
start = time.process_time()
one_and_half_algo()
end = time.process_time()
print("time taken for 1.5 approximation algorithm: ",end - start)


#genetic algorithm
print("\ngenetic algorithm: \n\n")
start = time.process_time()
genetic()
end = time.process_time()
print("time taken for 1.5 approximation algorithm: ",end - start)