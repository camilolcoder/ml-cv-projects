
#test_list = [6,1,3,2,4,7]
test_list = [3, 8, 2, 4, 11, 1, 2, 12]
#[2,7,1,4,11]

# [3, 8, 2, 4, 11, 1, 2, 12]

def maxProfit(prices) -> int:
    #Worst escenario the prices keep descending
    #Best they keep ascendint (Hence I need to keep the first value)
    #[4, 3, 2, 4, 1, 8, 7]
    #
    best_profit = 0
    low_baller = 1000000
    even_lower = 1000000
    for i in range(len(prices) - 1):

        actual_value = prices[i+1] - prices[i]
        new_value = prices[i+1] - low_baller
        new_lower = prices[i]
        if new_lower < even_lower:
            even_lower = new_lower
        print(actual_value, new_value, low_baller, even_lower)
        if new_value >= best_profit:
            best_profit = new_value
        if actual_value >= best_profit:
            low_baller = prices[i]
            best_profit = actual_value
        
        
    return best_profit

print(maxProfit(test_list))