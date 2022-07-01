dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice1) * len(dice2)
total_possibilities = 0

# Verify possibilities
for i in range(len(dice1)):
    for j in range(len(dice2)):
        if (dice1[j] + dice1[i]) <= 9:
          total_possibilities = total_possibilities + 1
          
# Get probability
probability = total_possibilities / total
print(f'Probability: {total_possibilities}/{total} = {probability}')