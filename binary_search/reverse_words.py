def reverse_string(s):
    ans = ""
    i = 0
    first_word = True
    while i < len(s):
        while i < len(s) and s[i] == " ":
            i += 1
        
        prev = i
        
        while i < len(s) and s[i] != " ":
            i += 1
        if s[prev:i]:
            if first_word:
                ans = s[prev:i] + ans
                first_word = False
                continue
            ans = s[prev:i] + " " + ans
    return ans


class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i = len(s) - 1
        
        while i >= 0:
            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0:
                break
            end = i
            while i >= 0 and s[i] != " ":
                i -= 1
            word = s[i + 1:end + 1]
            if result != "":
                result += " "
            result += word
        
        return result


if __name__ == "__main__":
    print(reverse_string("  This      is                me  "))
    obj = Solution()
    s = " amazing       coding skills       "
    print(obj.reverseWords(s))
