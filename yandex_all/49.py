class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_str = {}
        if len(strs) == 1:
            return [strs]
        else:
            for string in strs:
                current_key = str(sorted(string))
                if current_key in hash_str.keys():
                    hash_str[current_key].append(string)
                else:
                    hash_str[current_key] = []
                    hash_str[current_key].append(string)
            answer = list(hash_str.values())
            return answer
