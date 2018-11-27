class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for char in strs:
            sort_char = ''.join(sorted(char))
            if sort_char in dic:
                dic[sort_char] = dic[sort_char] + [char]
            else:
                dic[sort_char] = [char]
        return (list(dic.values()))
