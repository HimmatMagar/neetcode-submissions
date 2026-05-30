class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s, counter_t = Counter(s), Counter(t)

        return True if counter_s == counter_t else False