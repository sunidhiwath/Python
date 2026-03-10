# Taking integers from user and storing them in a tuple
nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(nums))

# b) Last item in the tuple
print("Last item:", nums[-1])

# c) Tuple in reverse order
print("Tuple in reverse order:", nums[::-1])

# d) Check if 5 is present
if 5 in nums:
    print("Yes")
else:
    print("No")

# e) Remove first and last item, sort remaining items
new_tuple = nums[1:-1]
sorted_tuple = tuple(sorted(new_tuple))
print("Tuple after removing first and last item and sorting:", sorted_tuple)

# Taking prices of sold items
prices = tuple(map(int, input("Enter prices of sold items separated by space: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Cheapest item price
print("Cheapest item price:", min(prices))

# c) Costliest item price
print("Costliest item price:", max(prices))

# d) Price list in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
costliest = max(prices)
count = prices.count(costliest)
print("Number of costliest items sold:", count)