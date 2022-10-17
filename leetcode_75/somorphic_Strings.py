class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_alph = {}
        set_letters = set()
        if len(s) != len(t):
            return false
        else:
            for el_s, el_t in zip(s, t):
                if el_s in dict_alph.keys():
                    if el_t != dict_alph[el_s]:
                        return False
                else:
                    if el_t not in set_letters:
                        dict_alph[el_s] = el_t
                        set_letters.add(el_t)
                    else: 
                        return False
            return True
