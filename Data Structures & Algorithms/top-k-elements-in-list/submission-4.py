class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}

        for l in nums:
            if l not in buckets:
                buckets [l] = 0
            buckets [l] += 1

        bucket_k = sorted([(buckets[k], k) for k in buckets], reverse = True) [:k]
        top_bucket_k = [e[1] for e in bucket_k]

        top_k = []
        for j in buckets:
            if j in top_bucket_k:
                top_k.append(j) 
        return top_k