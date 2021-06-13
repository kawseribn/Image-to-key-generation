#conributors:
#Palak Singhal 16co129
#Govind Jeevan

import random 
import hashlib
import time
import matplotlib.pyplot as plt 
import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
from main import Main_class

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d
# function to find extended gcd
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

# function to find modular inverse
def inverse(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m

# function to generate prime numbers
def generateprime(a,b):
	count=0
	while count<1:
		p= random.randint(a,b)
		if is_probable_prime(p):
			count+=1
	while count<2:
		q= random.randint(a,b)
		if is_probable_prime(q):
			if q!=p:
				count+=1
	return p,q


_mrpt_num_trials = 5 # number of bases to test
 
#To check if the number is prime
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


# To calculate gcd of two numbers
def gcd(a,b):
	while b!=0:
		a,b = b, a%b
	return a

# To generate keys e and d using prime numbers p and q
def generatekey(p,q):
    n= p*q
    phi = (p-1)*(q-1)
    g= 10
    while(g!=1):
        e= random.randrange(1,phi)
        g= gcd(e, phi)

    d= inverse(e, phi)

    return ((e,n), (d,n))

# Calculate xor of plaintext with key as well as ciphertext with key.
def xor(s1, s2):
 return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(pow(ord(char),key,n)) for char in plaintext]
    ciphertext = [str(int(char2)) for char2 in cipher]
    print(hex(int((''.join(ciphertext)))))
    #Return the array of bytes
    print(hashlib.sha256(str(cipher).encode('utf-8')).hexdigest())
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(char, key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)

def cipher(words,e,n): # get the words and compute the cipher
    tam = len(words)
    i = 0
    lista = []
    while(i < tam):
        letter = words[i]
        k = ord(letter)
        # k = k**e
        d = pow(k,e,n)
        lista.append(d)
        i += 1
    return lista    




def gen_key(img):

  lis = []
  n=1
  x=[]
  prime_object = Main_class(img)
  prime_num = prime_object.prime_numbers
  print(prime_num)
  keys = []

  start_time = time.time()
  p,q = prime_num[0],prime_num[1]
  print(p,q)
  # public, private = generatekey(p,q)
  Key1, Key2 = generatekey(p,q)
  print(f" Public Key: ({hex(Key1[0])},{hex(Key1[1])})")
  print(f" Private Key: ({hex(Key2[0])},{hex(Key2[1])})")

  keys.append(Key1)
  keys.append(Key2)

  return keys