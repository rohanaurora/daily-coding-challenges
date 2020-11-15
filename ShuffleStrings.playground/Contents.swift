import Cocoa

//Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
//Output: "leetcode"
//Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.


class Solution {
    func restoreString(_ s: String, _ indices: [Int]) -> String {
        
        var output = Array(s)
        let s = Array(s)
        
        for (index, value) in indices.enumerated() {
            output[value] = s[index]
        }
        
        return String(output)
    }
}

let s = "codeleet"
let i = [4,5,6,7,0,2,1,3]
let sol = Solution()
print(sol.restoreString(s, i))

