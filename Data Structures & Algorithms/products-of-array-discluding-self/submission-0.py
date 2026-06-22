class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        for indexi, i in enumerate (nums):
            product_element = 1
            for indexj, j in enumerate (nums):
                if  indexi != indexj:
                    product_element *= j
            product.append (product_element)

        return product
        