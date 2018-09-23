# HW1
# Group 001
import random
import time
bearcatii = {" ": 0}
def constr_bearcatii():
    for i in range(26):
        char = ord('a') + i
        bearcatii[chr(char)] = i + 1
constr_bearcatii()
#print("bearcattii",bearcatii)
bearcatii_inv = {v: k for k, v in bearcatii.items()}
#print("bearcatii_inv",bearcatii_inv)
# Converts a string to bearcatii
def convert_S_to_B(s):
    b = []
    for c in s.lower():
        b.append(bearcatii[c])
    return b
def convert_B_to_S(b):
    s = []
    for c in b:
        #print("C:", c)
        s.append(bearcatii_inv[c])
    return s
# Converts a list of numbers from base pow to base 10
def to_base_ten(list_of_nums, pow=27):
    sum = list_of_nums[0]
    for num in list_of_nums[1:]:
        sum = sum*pow + num
    return sum

# Converts a number from decimal to base in list form
def from_base_ten(num, base=27):
    nums = []
    while num > 0:
        mod = num % base
        nums.append(mod)
        num = num // base
    return nums[::-1]

def EuclidGCD(a, b):
    if a % b == 0:
        return b
    return EuclidGCD(b, a % b)



def ExtendedEuclidGCD(a,b):
    if (a==0):
        return (b,0,1) # return = a*x + b*y = gcd so return pair is (gcd,x,y)
    else:
        g,x,y = ExtendedEuclidGCD(b%a,a)
        return (g,y-(b//a)*x,x)


def EuclidsMultiplicativeInverse(e,phi):
    g,x,y = ExtendedEuclidGCD(e,phi)
    if (g==1):
        return x % phi

def MillerRabinPrimalityTest(n):
    #Output: always a composite when false is returned, probably correct when true is returned
    #Special Cases
    if (n == 1 or n ==2):
        return True
    if (n < 0 or n%2 == 0):
        return False
    #find postivie integers k,m suc that n-1 = (2^k)m and m is odd
    m = n-1
    k = 0

    while (m%2 == 0):
        k+=1
        m//=2
    #print("K = " + str(k) + " m = " + str(m))
    assert(2**k *m == n-1)

    a = random.randint(2,n-1) # not inclusive on end

    # To increase correctness, check multiple times
    for i in range(5):
        a = random.randint(2, n - 1)  # not inclusive on end
        if (isComposite(a,m,n,k)):
            return False
    return True

def generateKeys(p,q):
    #Ensure that both values are prime
    if (not MillerRabinPrimalityTest(p) or not MillerRabinPrimalityTest(q)):
        return  None
    n = p * q

    phi = (p-1) * (q-1)

    #pick random e to find a number coPrime to phi
    publicKey = random.randint(1, phi)
    g = EuclidGCD(publicKey, phi)
    while g != 1:
        publicKey = random.randint(1, phi)
        g = EuclidGCD(publicKey, phi)
        #print("PickedNewPublicKey",publicKey)

    privateKey = EuclidsMultiplicativeInverse(publicKey,phi)
    #print("MultiplicativeInverseIs", privateKey)
    return ((publicKey,n),(privateKey,n))

def isComposite(a, m, n, k):
    b = pow(a, m, n)
    if (b == 1):
        return False
    for _ in range(k):
        b = b * b % n
        if (b == n - 1):
            return False
    if (b != 1):
        return True
    else:
        return False

def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

def encrpyt_text(input, key,n):
    bearcatiiInput = convert_S_to_B(input)
    print("BEARCATII",bearcatiiInput)
    encrpytedText = []
    for x in bearcatiiInput:
        #print("X:",x)
        encrpytedText.append(pow(x%n,key%n)%n)
        #print("ENCRYTED", encrpytedText)
    #print("ENCRYTED",encrpytedText)
    return encrpytedText

def decrypt_text(ciper,key,n):
    plainText = []
    for x in ciper:
        plainText.append(pow(x%n,key%n)%n)
        #print("Pl",plainText)
    #print("Plaintext", plainText)
    return plainText

minPrime = 1
maxPrime = 1000#00000
#Get random number p which is prime
p = -1
while p < 0:
    temp = random.randint(minPrime,maxPrime)
    if MillerRabinPrimalityTest(temp) == True:
        p = temp

print("DebugP:",p)
#Get random number q which is prime
q = -1
while q < 0:
    temp = random.randint(minPrime,maxPrime)
    if MillerRabinPrimalityTest(temp) == True:
        q = temp
print("DebugQ:",q)
publicKey, privateKey = generateKeys(p, q)
print("DebugPublic:", publicKey)
print("DebugPrivate:", privateKey)
key,n = publicKey
message = input("Enter Message: ")
cipher = encrpyt_text(message,key,n)
key,n = privateKey
decryptedInput = decrypt_text(cipher,key,n)
print("DebugDecrypted:",decryptedInput)

print("P:",p)
print("Q:",q)
print("N:",n)
print("M:",message)
print("C:",cipher)
print("P:", ''.join(convert_B_to_S(decryptedInput)))