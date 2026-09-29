Initial thoughts:
Iterate through arr once and add every integer to a hash set. Then iterate again and check in O(1) if x + 1 is in the hash_set. Return the coutn.