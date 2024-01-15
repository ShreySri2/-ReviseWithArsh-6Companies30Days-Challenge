class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        cache = [0]*n
        cache[0]=1

        MOD = 10 ** 9 + 7

        old_sharers = 0

        for i in range(1,n):
            new_sharers = cache[i-delay]
            people_forget = cache[i-forget]
            cache[i] = old_sharers + new_sharers - people_forget
            old_sharers = cache[i]
        return sum(cache[-forget:])%MOD
        