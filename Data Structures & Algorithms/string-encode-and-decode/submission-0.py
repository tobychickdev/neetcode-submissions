class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            length = len(s)
            parts.append(str(length)+"#"+s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        current_num = ""
        decoded_string = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                current_num += s[i]
                i += 1
                continue
            if s[i] == "#":
                decoded_string.append(s[i+1:(i+1+int(current_num))])
                i = i + 1 + int(current_num)
                current_num = ""
                continue
            i += 1
        return decoded_string
