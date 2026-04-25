# set_nums = set(nums)
        # lost = []

        # for i in range(1,len(nums)+1):
        #     if i not in set_nums:
        #         lost.append(i)
            
        # return lost

        n = len(nums)+1
        seen = [False]*n
        for i in nums:
            seen[i] = True
        return [i for i in range(1,n) if not seen[i]]