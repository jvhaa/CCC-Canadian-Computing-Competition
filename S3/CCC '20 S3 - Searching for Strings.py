import sys
input = sys.stdin.read

MOD = int(10e9 + 7)

def main():
    data = input().split()
    N = data[0]
    H = data[1]
    
    n = len(N)
    m = len(H)
    
    hsh = [0] * (m + 1)
    hsh2 = [0] * (m + 1)
    pw = [1] * (m + 1)
    pw2 = [1] * (m + 1)
    
    base = 2
    base2 = 3
    
    freq = [0] * 26
    freq2 = [0] * 26
    
    for char in N:
        freq[ord(char) - ord('a')] += 1
    
    for i in range(1, m + 1):
        hsh[i] = (hsh[i - 1] * base + ord(H[i - 1])) % MOD
        pw[i] = pw[i - 1] * base % MOD
        hsh2[i] = (hsh2[i - 1] * base2 + ord(H[i - 1])) % MOD
        pw2[i] = pw2[i - 1] * base2 % MOD
    
    def get_substr_hash(l, r):
        h1 = (hsh[r] - hsh[l + 1] * pw[r - l - 1] % MOD) % MOD
        h2 = (hsh2[r] - hsh2[l + 1] * pw2[r - l - 1] % MOD) % MOD
        return (h1 << 31) | h2
    
    seen_hashes = set()
    
    for i in range(1, m + 1):
        freq2[ord(H[i - 1]) - ord('a')] += 1
        if i > n:
            freq2[ord(H[i - n - 1]) - ord('a')] -= 1
        if freq == freq2:
            seen_hashes.add(get_substr_hash(i - n - 1, i))
    
    print(len(seen_hashes))

if __name__ == "__main__":
    main()
