#!/usr/bin/env python
best_score = __import__('Biggest_keys').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'mike': 14, 'molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best Score: {}". format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
