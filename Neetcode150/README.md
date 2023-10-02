# Neetcode 150 Table

## Array and Hashing
| Problem                                                                           | Notes                                                                                                                   |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [Contains Duplicate](Array-and-Hashing/contains-duplicate.md)                     | Use a hashSet to detect duplicates.                                                                                     |
| [Valid Anagram](Array-and-Hashing/valid-anagram.md)                               |                                                                                                                         |
| [Two Sum](Array-and-Hashing/two-sum.md)                                           |                                                                                                                         |
| [Group Anagrams](Array-and-Hashing/group-anagrams.md)                             | Hashmap[tuple(countOfLetters)] = list of anagrams                                                                       |
| [Top K Frequent Elements](Array-and-Hashing/top-k-frequent-elements.md)           | HashMap counter, then put it into bucket sort array with index as counter(val). Reverse for loop                        |
| [Product of Array except Self](Array-and-Hashing/product-of-array-except-self.md) | Calculate prefix and postfix to get the answer.                                                                         |
| [Longest Consecutive Sequence](Array-and-Hashing/longest-consecutive-sequence.md) | Make a set, check if it is the start of the sequence, count the length of the sequence, return the max of these counts. |
| [Valid Sudoku](Array-and-Hashing/valid-sudoku.md)                                 | Make 3 defaultdict of sets, if the position already exists in one of the sets, return false.                            |

# Two Pointers
| Problem                                           | Notes                                                                                        |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [Valid Palindrome](Two-Pointers/valid-palindrome.md) | Two pointers, traversing to middle, return true if they pass eachother. |