// An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

func isAnagram(firstWord: String, secondWord: String) -> Bool {
    return stringToDict(firstWord) == stringToDict(secondWord)
}

func stringToDict(_ s:String) -> [Character:Int] {
    var dict = [Character:Int]()
    s.forEach {
        if let count = dict[$0] {
            dict[$0] = count + 1
        } else {
            dict[$0] = 0
        }
    }
    return dict
}

print(isAnagram(firstWord: "cat", secondWord: "tac")) // -> True
print(isAnagram(firstWord: "aaabbb", secondWord: "ab")) // -> False
print(isAnagram(firstWord: "aabbccdd", secondWord: "ddccaabb")) // -> True
print(isAnagram(firstWord: "aabbc", secondWord: "cccab")) // -> False
