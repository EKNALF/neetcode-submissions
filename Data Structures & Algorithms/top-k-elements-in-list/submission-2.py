class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for element in nums:
            counts[element] = counts.get(element, 0) + 1

        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        output = []

        return list(sorted_counts.keys())[:k]