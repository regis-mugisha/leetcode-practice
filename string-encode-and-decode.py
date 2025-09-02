from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, result = [], ""
        for s in strs:
            sizes.append(str(len(s)))

        for size in sizes:
            result += size
            result += ","
        result += "#"

        for s in strs:
            result += s

        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, result, i = [], [], 0

        while s[i] != "#":
            # assume length contains more than one digit
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1  # skip the '#'

        for size in sizes:
            result.append(s[i : i + size])
            i += size
        return result


strs = ["neet", "code", "love", "you"]

solution = Solution()
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
print(decoded)
