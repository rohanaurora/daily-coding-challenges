import Cocoa

/*
 
https://leetcode.com/articles/reverse-words-in-a-string/
 
 Input: s = "the sky is blue"
 Output: "blue is sky the"

*/

class Solution {
    func reverseWords(_ s: String) -> String {
        let wordsArray = s.components(separatedBy: " ")

        var output: [String] = []

        for arrayIndex in stride(from: wordsArray.count - 1, through: 0, by: -1) {
            output.append(wordsArray[arrayIndex])
        }

        output = output.filter({ !$0.isEmpty})
        return output.joined(separator: " ").trimmingCharacters(in: .whitespaces)
    }
}

let input = "a good   example"
let solution = Solution()
print(solution.reverseWords(input))


