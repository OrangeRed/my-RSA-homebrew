import random


"""Global variables"""
BITS = 512


"""Return True if a candidate is likely to be prime"""
def millerRabin(candidate):

    # Edge Cases
    # If candidate is 2 or 3, it is prime. If candidate is even, it is not prime
    if candidate == 2 or candidate == 3:
        return True
    if candidate % 2 == 0:
        return False

    # d*2^r = candidate - 1
    # While `d` is even keep dividing by two to find `r` 
    r, d = 0, candidate - 1
    while d % 2 == 0:
        r += 1
        d = d // 2

    # Create witness `a` between {2 . . . candidate - 2} and compute a^d mod candidate
    a = random.randint(2, candidate - 2)
    x = pow(a, d, candidate)

    # if a^d mod candidate == 1 or a^d mod candidate == -1, the candidate is prime
    if x == 1 or x == candidate - 1:
        return True

    # Check all squares of a^(d*2^r) mod candidate 
    for _ in range(r - 1):
        x = pow(x, 2, candidate)

        # if a^(d*2^r) mod candidate == 1, the candidate is not prime
        if x == 1:
            return False 
        
        # if a^(d*2^r) mod candidate == -1, the candidate is prime
        if x == candidate - 1:
            return True
    
    # otherwise the candidate is likely not prime
    else:
        return False
    

"""Return a random integer of length `bits` that passes the Miller-Rabin test"""
def getPrimeCandidate(bits):
    while True:
        candidate = random.getrandbits(bits)
        if millerRabin(candidate):
            return candidate


"""Return GCD of two integers using Euclidean Algorithm"""
def gcd(a, b):

    # While the remainder is not zero, set a = b and b = remainder of a // b
    while b:
        a, b = b, a % b 
    return a


"""Return coefficient of `x` using Extended Euclidean Algorithm"""
def gcdExtended(a, b):
    
    # Initialize `x` and `y` coefficients
    prevx, x = 1, 0
    prevy, y = 0, 1

    # While the raminder is not zero, keep track of GCD coefficients and perform GCD
    while b:
        quotient = a // b
        x, prevx = prevx - quotient * x, x
        y, prevy = prevy - quotient * y, y
        a, b = b, a % b

    # Return coefficient of `x` when remainder becomes zero
    return prevx


"""Return a random integer between {1 . . . phiN - 1} that has GCD equal to 1 with phiN"""
def getEncrptionExponent(phiN):
    while True:
        e = random.randint(1, phiN - 1)
        if gcd(e, phiN) == 1:
            return e


"""Return the result of modular exponentiation"""
def squareMultiply(base, exponent, modulus):

    # Initialize result
    result = 1

    # Reduce base to prevent from getting to large
    base = base % modulus

    # Edge case with base == 0
    if (base == 0):
        return 0

    # While the exponent > 0 perform square and multiply
    while (exponent > 0):

        # if exponent is odd multiply
        if (exponent % 2 == 1):
            result = (result * base) % modulus

        # otherwise square
        base = (base * base) % modulus 
        
        # Divide exponent by two rounded down
        exponent = exponent // 2

    # return result of square and multiply
    return result 


"""Only run this script if called directly"""
if __name__ == "__main__":

    # Get two random prime integers of length BITS
    p = getPrimeCandidate(BITS)
    print(f"Random {BITS}-bit Prime p: {p}")
    q = getPrimeCandidate(BITS)
    print(f"Random {BITS}-bit Prime q: {q}\n")

    # Calculate N, phiN using prime integers
    N = p * q
    print(f"N = p * q = {N}\n")
    phiN = (p - 1) * (q - 1)
    print(f"phiN = (p-1)(q-1) = {phiN}\n")

    # Get a random integer `e` between {1 . . . phiN - 1} with GCD(e, phiN) = 1
    e = getEncrptionExponent(phiN)
    print(f"e: {e}\n")

    # Calculate `d` using Extended Euclidean Algorithm
    d = gcdExtended(e, phiN) % phiN
    print(f"d = e^-1 mod phiN = {d}\n\n")

    # Hard coded message
    msg = 13
    print(f"RSA Message: {msg}")

    # Encrypt and Decrypt message using modular exponentiation
    enc = squareMultiply(msg, e, N)
    print(f"Encrypted: {enc}")
    dec = squareMultiply(enc, d, N)
    print(f"Decrypted: {dec}")

