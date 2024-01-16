class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_c = Counter(list(secret))
        guess_c = Counter(list(guess))

        cow = 0
        for key in guess_c.keys():
            if key in secret_c:
                cow+= min(guess_c[key], secret_c[key])
        bull = 0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
                cow-=1
        return str(bull)+'A'+ str(cow)+'B'