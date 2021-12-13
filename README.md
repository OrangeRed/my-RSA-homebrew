# Usage Guide

### Python version 3 or higher is required to continue with this guide

Get the lastest version of Python: https://www.python.org/downloads/
<br/>

## Inside of the project directory

Run RSA keygen, encryption, decryption with:

```
python RSA.py
```

## Explanation

Two random 512 bits integers `p` and `q` that pass the [Miller-Rabin Primality Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

Calculate `N = p * q` and `phiN = (p-1)(q-1)`

Generate `e` such that it is between `{1 . . . phiN - 1}` with `GCD(e, phiN) = 1`

Generate `d = e^-1 mod phiN`

Encrypt message `ENC = MSG^e mod N`

Decrypt message `MSG = ENC^d mod N`
