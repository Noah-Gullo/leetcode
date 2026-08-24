# 2396. Strictly Palindromic Number
## Link
https://leetcode.com/problems/strictly-palindromic-number/description/?envType=problem-list-v2&envId=two-pointers

## Info
Medium/90.4% Acceptance/195,341 out of 216,100 accepted
Topics: Senior, Math, Two Pointers, Brainteaser, Biweekly Contest 86

## Description
2396. Strictly Palindromic Number
Medium
Topics
premium lock icon
Companies
Hint
An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
Example 2:

Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.

 

Constraints:

4 <= n <= 105
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
195,341/216.1K
Acceptance Rate
90.4%