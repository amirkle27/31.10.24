import numpy as np

#1
#a
numbers = np.arange(1,11)
print("1.a",numbers)

#b
numbers2 = np.arange(0.5,5,0.25)
print("1.b",numbers2 )

#2
#a
zeros = np.zeros(10)
print("2.a",zeros)

#b
zeroes_3_4 = np.zeros(shape=(3,4))
print(f"2.b\n",zeroes_3_4)

#3
#a
lin1 = np.linspace(2,12,5)
print("3.a",lin1)

#b
lin2 = np.linspace(3,9,4)
print("3.b",lin2)

#4
#a
rand_nums = np.random.rand(4,2)
print(f"4.a\n",rand_nums)

#b
rand_ints = np.random.randint(10,21,(3,3))
print(f"4.b\n",rand_ints)
rand_ints_reshaped = rand_nums.reshape(1,8)
print("4.b - reshaped - ",rand_ints_reshaped)

#5
"""By using a constant seed, we can maintain the list of random numbers generated. 
Each specific seed creates a list of random numbers, which we can later save, edit, use or manipulate for other uses.
The advantage in using seeds in the random operation is that the numbers generated every time you run the code will be the same"""
