import numpy as np

def unit_step(v):
	""" Heavyside Step function. v must be a scalar """
	if v >= 0: 
		return 1
	else: 
		return 0
		
def perceptron(x, w, b):
   
	v = np.dot(w, x) + b
	y = unit_step(v)
	return y

def NOT_percep(x):
	return perceptron(x, w=-1, b=0.5)

print("NOT(0) = {}".format(NOT_percep(0)))
print("NOT(1) = {}".format(NOT_percep(1)))


def AND_percep(x):
    w = np.array([1, 1])
    b = -1.5
    return perceptron(x, w, b)


example1_and = np.array([1, 1])
example2_and = np.array([1, 0])
example3_and = np.array([0, 1])
example4_and = np.array([0, 0])

print("AND(1, 1) = "+str(AND_percep(example1_and)))
print("AND(1, 0) = "+str(AND_percep(example2_and)))
print("AND(0, 1) = "+str(AND_percep(example3_and)))
print("AND(0, 0) = "+str(AND_percep(example4_and)))

def OR_percep(x):
    w = np.array([1, 1])
    b = -0.5
    return perceptron(x, w, b)


example1_or = np.array([1, 1])
example2_or = np.array([1, 0])
example3_or = np.array([0, 1])
example4_or = np.array([0, 0])

print("OR({}, {}) = {}".format(1, 1, OR_percep(example1_or)))
print("OR({}, {}) = {}".format(1, 0, OR_percep(example2_or)))
print("OR({}, {}) = {}".format(0, 1, OR_percep(example3_or)))
print("OR({}, {}) = {}".format(0, 0, OR_percep(example4_or)))
