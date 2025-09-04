# Coin Change Algorithm
# Implemented by William M Mortl

# O(coins * amount)
# python coinChange.py 6 "1,4,3"

# imports
import sys

# coin change algorithm, uses dynamic programming
def coinChange(amount, coins):
	adjAmount = int(amount * 100)
	adjCoins = list(map(lambda x: int(x * 100), coins))
	k = len(adjCoins)
	C = [0] * (adjAmount + 1)
	S = [0] * (adjAmount + 1)
	for p in range(min(adjCoins), (adjAmount + 1)):
		minVal = float('inf')
		coin = 0
		for i in range(0, k):
			if (adjCoins[i] <= p):
				if ((C[p - adjCoins[i]] + 1) < minVal):
					minVal = 1 + C[p - adjCoins[i]]
					coin = i
		C[p] = minVal
		S[p] = coin
	return [makeChange(S, coins, amount), C, S]

# make change from the dynamic programming results
def makeChange(S, coins, amount):
	adjAmount = int(amount * 100)
	change = []
	while adjAmount > 0:
		change.append(coins[S[adjAmount]])
		adjAmount = adjAmount - int(coins[S[adjAmount]] * 100)
	return change

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nCoin Change by William M Mortl")
		print("Usage: python coinChange.py {amount to change} \"{comma seperated list of currency values}\"")
		print("Example: python coinChange.py 3.37 \".5, .25, .10, .05, .01\"\r\n")
	else:
		amountToChange = float(sys.argv[1])
		currencies = list(map(float, sys.argv[2].split(",")))
		if (min(currencies) > amountToChange):
			print("\r\nCannot change, coins too big!\r\n")
		else:
			[change, C, S] = coinChange(amountToChange, currencies)
			print("\r\nC matrix:\r\n{}".format(C))
			print("S matrix:\r\n{}".format(S))
			print("\r\nChanging {}: {}".format(amountToChange, change))
			print("Sum of coins: {}\r\n".format(sum(change)))
