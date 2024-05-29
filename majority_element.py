class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele_count=Counter(nums)
        majority_ele=[]
        N=len(nums)//3
        for element,count in ele_count.items():
            if count >N:
                majority_ele.append(element)
        return majority_ele


        