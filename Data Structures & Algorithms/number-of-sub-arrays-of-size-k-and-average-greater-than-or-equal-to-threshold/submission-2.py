class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        window_sum=0

        for i in range(k):
            window_sum += arr[i]
        
        avg = window_sum/k
        if avg >= threshold:
            count +=1

        for i in range(k,len(arr)):
            window_sum = window_sum - arr[i-k] + arr [i]
        
            avg = window_sum/k

            if avg >= threshold:
                count +=1

        return count


            

        

        


            