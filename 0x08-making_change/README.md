# Coin Change problem

# Overview

This project provides a solution to the coin change problem, which determine the fewest number of coins needed to make a specific total using a given se of coin denominations.

## Function Prototype

```Python
def makeChange(coins, total)
```
### Parameters

* ``coins``: A list of integers representing the values of the coins available.
* ``total``: An integer representing the target amount of money.

### Returns

* The fewest number of coins needed to meet the total.
* If the total is 0 or less, the function returns 0.
* If the total cannot be met by any comibination of the coins, it returns -1.

### Assumptions

* Each coin's value is an integer greater than 0.
* There is an infinit supply of each denomination of coin.

### Example 

```python
coinse = [1, 2, 5]
total = 11
result = makeChange(coins, total) # Output: 3(11 = 5 + 5 + 1)
```

### Runtime Complexity

The runtime complexity of this solution is 0(n *m), where n is the number of coin denominations and m is the total amount. This is due to the nested loops iterating coin and each amount up to the total.

### Usage
You can use this function by importing it into your Python script or running environment. Make sure to provide the appropraite list of coins and desired total.
