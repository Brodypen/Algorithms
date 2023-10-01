---
status: 
tags:
  - review
  - LC_Medium
sr-due: 2023-10-02
sr-interval: 1
sr-ease: 230
---

<mark style="background: #FF5582A6;">Next review: Do neetcode flash cards.</mark>

# Valid Sudoku
```ad-tldr
title: Psuedo Solution
collapse: closed
- Create 3 hashMaps of set (defaultdict(set))
- Hashmaps have this type of format
	- Cols = Key: c, value: board[r][c]
	- Rows = Key: r, value: board[r][c]
	- squares = Key: (r//3, c//3), value: board[r][c]
- Loop through the matrix.
- Check if it is a number, then check if it isnt already in a set.
	- Return False, if it is part of a set.
- Add position to Hashmap
- If you get through the whole matrix, that means it is true.

```
## Problem statement
Prove that a sudoku board is valid.

### Solution
```ad-tldr
title: Solution
collapse: closed

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
        

```

---
##### Cue Flashcards 🗃

---
# References
1. https://leetcode.com/problems/valid-sudoku/description/

