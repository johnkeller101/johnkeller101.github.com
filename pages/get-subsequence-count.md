---
layout: page
current: about
title: getSubSequenceCount Interview Question
navigation: true
class: page-template
subclass: 'post page'
cover:
cover-height: 400

date: 2022-10-25 20:50:00

---

#### Getting Started
----------

##### Example
```
s1 = "ABC"
s2 = "ABCBABC"
```
The string `s1` appears 5 times as a subsequence in `s2` at 1- indexed positions of (1, 2, 3), (1, 2, 7), (1, 4, 7), (1, 6, 7), and (5, 6, 7). The answer is 5.

##### Function Description
Complete the function `getSubsequenceCount` in the editor below.

`getSubsequenceCount` has the following parameters:
- string `s1`: the first string, which always has a length of 3
- string `s2`: the second string

Returns:
- int: the number of times `s1` appears as a subsequence in `s2`

##### Constraints
- length of `s1` = 3
- 1 ≤ length of `s2` ≤ 5 * 10^5
- `s1` and `s2` consist of uppercase English letters, A-Z.

#### Answer
----------

```
// Complete the 'getSubsequenceCount' function below.
// The function is expected to return a LONG_INTEGER.
// The function accepts following parameters:
// 1. STRING s1
// 2. STRING s2

func getSubsequenceCount(s1: String, s2: String) -> Int {
    let set = CharacterSet.init(charactersIn: s1)
    let cleanedS2 = s2.trimmingCharacters (in: set.inverted)
    let s2Array = Array(cleanedS2)

    var matches: [String] = []
    for i in 0...cleanedS2.count-3 {
        for j in 1...cleanedS2.count-2 {
            for k in 2...cleanedS2.count-1 {
                let str = "\(s2Array[i])\(s2Array[j])\(s2Array[k])"
                let match = "\(i)\(j)\(k)"
                if i < j && j < k && str == s1 && !matches.contains(match) {
                    matches.append(match)
                }
            }
        }
    }
    return matches.count
}


runTestCase(number: 1, expected: 3, s1: "HRW", s2: "HERHRWS")
runTestCase(number: 2, expected: 2, s1: "LKL", s2: "KKMKMKKKKKMMLMKKMMML")
runTestCase(number: 3, expected: 4, s1: "ELO", s2: "HELLOWORLD")
runTestCase(number: 4, expected: 5, s1: "ABC", s2: "ABCBABC")

func runTestCase(number: Int, expected: Int, s1: String, s2: String) {
    let test = getSubsequenceCount(s1: s1, s2: s2)
    if test == expected {
        print("Test \(number) Passed (got \(test), expected \(expected))")
    } else {
        print("Test \(number) FAILED (got \(test), expected \(expected))")
    }
}
```