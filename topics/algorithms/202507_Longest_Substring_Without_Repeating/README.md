# Longest Substring Without Repeating Characters

## Problem Statement
Write a function that finds the length of the longest substring within a given string that doesn't have any repeating characters.

## Key Concepts
- A **substring** is a continuous sequence of characters within the original string
- **Repeating characters** means the same character appears more than once
- The substring must be continuous (unlike a subsequence which can skip characters)

## Examples

### Example 1
```
Input: s = "abcabcbb"
Output: 3
Explanation: 
- The longest substring without repeating characters is "abc"
- Length is 3
- Other valid substrings are "bca", "cab", but none are longer
```

### Example 2
```
Input: s = "bbbbb"
Output: 1
Explanation:
- Since all characters are the same ('b'), any substring with length > 1 would have repeats
- Therefore, the longest valid substring is just "b"
- Length is 1
```

### Example 3
```
Input: s = "pwwkew"
Output: 3
Explanation:
- The longest substring without repeats is "wke"
- Length is 3
- Note: "pwke" would be invalid as it's a subsequence, not a substring
- The difference is that substrings must be continuous
```

## Important Notes
- The solution should return the LENGTH of the substring, not the substring itself
- Empty strings are valid inputs
- Spaces count as characters
- The string can contain any combination of letters, numbers, symbols, and spaces

## Constraints
- String length: 0 ≤ length ≤ 50,000
- Valid characters: English letters, digits, symbols, and spaces
