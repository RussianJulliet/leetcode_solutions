class Solution:
    def compress(self, chars):
        n = len(chars)
        if n != 1:
            for i in range(n):
                cur_char = chars[i]
                if i == 0:
                    next_char = chars[i+1]
                    count = 1
                    if next_char != cur_char:
                        chars.append(cur_char)
                elif i == (n - 1):
                    prev_char = chars[i-1]
                    if prev_char == cur_char:
                        count += 1
                        chars.append(cur_char) 
                        count_str = str(count)
                        for elem_s in count_str:
                            chars.append(elem_s)
                    else:
                        chars.append(cur_char)
                else:
                    prev_char = chars[i-1]
                    next_char = chars[i+1]
                    if prev_char == cur_char:
                        count += 1
                        if next_char != cur_char:
                            if count != 1:
                                # chars[i] = count
                                chars.append(cur_char) 
                                count_str = str(count)
                                for elem_s in count_str:
                                    chars.append(elem_s)
                    else:
                        count = 1
                        if next_char != cur_char:
                            chars.append(cur_char)
            for i in range(n):
                chars.pop(0)
            return f"Return {len(chars)}, and the first {len(chars)} characters of the input array should be: {chars}"
        else:
            return f"Return 1, and the first character of the input array should be: {chars}"

sol = Solution()
print(sol.compress(["a","a","a","b","b","a","a"]))

