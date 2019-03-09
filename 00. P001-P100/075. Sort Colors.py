# 计数排序
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c0 + c1] = [1] * c1
        nums[c0 + c1:] = [2] * c2


# 解法2-申请两枚指针，head 和 tail，用 i 进行遍历，当 num[i] == 0时，
# 交换当前位置和头指针处值，当nums[i] == 2时，交换当前位置和尾指针处值，
# 当 nums[i] == 1时，不进行交换

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head, tail, i = 0, len(nums) - 1, 0
        while i <= tail:
            if nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                head += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1
            else:  # nums[i]为1时
                i += 1
