from onehalfopt import *
from BNB import *
from dptsp import *
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
onehalf([[0, 0],[3, 0],[6, 0],[0, 3],[3, 3],[6, 3],[0, 6],[3, 6],[6, 6],])
end = time.process_time()
print("time taken for 1.5 approximation algorithm: ",end - start)


