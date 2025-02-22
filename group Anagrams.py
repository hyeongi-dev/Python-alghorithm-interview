import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strs for문 돌려서 sorted 해서 dic_str 에 있는지 확인하고 있으면 애너그램으로 보고 없으면 애너그램 아님
        #dic_str key : sorted(str), value : [eat,tea,ate] 이런형식으로 저장
        #dic_str.value() 를 list로 변환해서 return하면 끝일듯?

        #dic value 값을 리스트로 저장어떻게 하는지?
        dic_str = defaultdict(list)

        for str in strs:
            sorted_str = ''.join(sorted(str))
            dic_str[sorted_str].append(str)

        return list(dic_str.values())
     