def dp_algo():
    cost = [[ 0,10, 8, 9, 7, 3,  5, 6, 9 ],
			[10, 0,10, 5, 6, 3 , 2, 1, 9 ],
			[ 8,10, 0, 8, 9 , 7, 3, 7, 2 ],
			[ 9, 5, 8, 0, 6 , 2, 5, 8, 4],
			[ 7, 6, 9, 6, 0, 5, 7, 3, 2],
			[ 3, 3, 7, 2, 5, 0, 2, 3, 4],
			[ 5, 2, 3, 5, 7, 2, 0, 3,4 ],
			[ 6, 1, 7, 8, 3, 3, 4, 0, 1 ],
			[ 9, 9, 2, 4, 2, 4, 4, 1, 0],

            ]
    n = 9
    visited_all = (1 << n)-1
    '''2d dp table to memorize all the results for a given value of mask and pos'''
    dp = [[]]
    dp = [[-1 for i in range(n)] for j in range(1 << n)]

    '''mask: denotes set of cities visited so far
    pos:index in mask or id of the city'''


    def tsp(mask, pos):
        '''when all cities are visited mask has all bits as 1'''
        if (mask == visited_all):
            return cost[pos][0]
        if (dp[mask][pos] != -1):
            return dp[mask][pos]
        ans = 999999
        for v in range(0, n):
            '''check if ith bit in mask (city)is visited or not'''
            if (mask & (1 << v)) == 0:
                newans = cost[pos][v]+tsp(mask | (1 << v), v)
                ans = min(ans, newans)
        dp[mask][pos] = ans
        return ans


    print('weight:', tsp(1, 0))

