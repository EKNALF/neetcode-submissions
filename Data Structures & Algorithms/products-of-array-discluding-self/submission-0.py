class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        elif zero_count == 1:
            non_zero_product = 1

            for num in nums:
                if num != 0:
                    non_zero_product *= num

            for num in nums:
                if num == 0:
                    products.append(non_zero_product)
                else:
                    products.append(0)

        else:
            total_product = 1

            for num in nums:
                total_product *= num

            for num in nums:
                products.append(total_product // num)

        return products