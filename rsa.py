import random
import time
import matplotlib.pyplot as plt 
import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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


def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a


def generatekey(p,q):
    n= p*q
    phi = (p-1)*(q-1)
    g= 10
    while(g!=1):
        e= random.randrange(1,phi)
        g= gcd(e, phi)

    d= inverse(e, phi)

    return ((e,n), (d,n))

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    lis = []
    x= []
    n=3
    while n<7:
        start_time = time.time()
        print "RSA Encrypter/ Decrypter"
        p,q = generateprime(2**n,2**(n+1))
        print p,q
        public, private = generatekey(p,q)
        print "Your public key is ", public ," and your private key is ", private
        '''message = raw_input("Enter a message to encrypt with your private key: ")'''        
        message= 'palak'
        encrypted_msg = encrypt(private, message)
        
        print "Your encrypted message is: "
        print ''.join(map(lambda x: str(x), encrypted_msg))
        print "Decrypting message with public key ", public ," . . ."
        print "Your message is:"
        print decrypt(public, encrypted_msg)
        print "--- %s seconds ---" % (time.time() - start_time)
        print "n: ", n
        x.append(n)
        lis.append(time.time()- start_time)
        times = 5
        while(times>0):
            e,n1= public
            d, n1= private
            print "d = ", d
        
            hacked_d = hack_RSA(e, p*q)
        
            if d == hacked_d:
                print "Hack WORKED!"
            else:
                print "Hack FAILED"
            
            print "d = ", d, ", hacked_d = ", hacked_d
            print "-------------------------"
            times -= 1
        n= n+1

    plt.plot(x, lis)
    plt.xlabel('Number of bits ')
    plt.ylabel('Time taken')
    plt.title('Bits in prime number vs time taken') 
    plt.show() 
    



    
