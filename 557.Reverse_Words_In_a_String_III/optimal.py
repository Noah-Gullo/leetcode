class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        ns=""
        for i in l:
            ns+=i[: :-1]+" "
        return ns.strip()