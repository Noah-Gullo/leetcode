# 844. Backspace String Compare

## Link
https://leetcode.com/problems/backspace-string-compare/description/

## Info
Easy/50.3% Acceptance/1,130,680 out of 2,200,000 accepted
Topics: Mid Level, Two Pointer, String, Stack, Simulation, Weekly Contest 87

## Description
844. Backspace String Compare
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,130,680/2.2M
Acceptance Rate
50.3%