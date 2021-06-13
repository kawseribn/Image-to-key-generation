import random 
import time
import matplotlib.pyplot as plt 

def generateprime(a,b):
	count=0
	while count<1:
		p= random.randint(a,b)
		if is_probable_prime(p):
			count+=1
	return p

_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

if __name__ == '__main__':
	
    lis = []
    x= []
    n1=1
    while n1<15:
        start_time = time.time()
        p= generateprime(2**n1,2**(n1+1))
        b= random.randint(500,5000)
        A= random.randint(500,5000)
        B= random.randint(500,5000)
        print("shared prime ",p, "shared base ",b)
        X= (b**A)%p
        Y= (b**B)%p
        print("Alice sends", X, "Bob sends", Y)
        m= (Y**A)%p
        n= (X**B)%p
        print("alice shared secret:  ", m, "      Bob shared secret:   ", n)
        print("--- %s seconds ---" % (time.time() - start_time))
        print ("n: ", n1)
        x.append(n1)
        lis.append(time.time()- start_time)
        n1= n1+1
    plt.plot(x, lis)
    plt.xlabel('Number of bits ')
    plt.ylabel('Time taken')
    plt.title('Bits in prime number vs time taken') 
    plt.show() 
    plt.savefig('dh-graph')