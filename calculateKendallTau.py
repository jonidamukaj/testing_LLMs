# Import required libraries
from scipy.stats import kendalltau
  
# Taking values from the above example in Lists
X = [1, 2, 3, 4, 5, 6, 7]
Y = [1, 3, 6, 2, 7, 4, 5]
  
# Calculating Kendall Rank correlation
corr, _ = kendalltau(X, Y)
print('Kendall Rank correlation: %.5f' % corr)
  
# This code is contributed by Amiya Rout