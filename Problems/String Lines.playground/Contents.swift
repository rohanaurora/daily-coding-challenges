import UIKit

// Number of Lines To Write String

class Solution {
    func numberOfLines(_ widths: [Int], _ S: String) -> [Int] {
        
        let stringArray = Array(S.map({$0}))
        let alphabets = (97...122).map({Character(UnicodeScalar($0))})
        let dictionary = Dictionary(uniqueKeysWithValues: zip(alphabets, widths))
        print(dictionary)
        
        var sum:Int = 0
        var output:[Int] = []

        for i in stringArray {
            sum = sum + dictionary[i]!
        }
        
        let lines = sum/100
        let remainder = (sum % 100)
        if remainder > 0 {
            output.append(lines + 1)
            let lastElement = remainder > widths.last! ? remainder: dictionary[(S.last!)]!
            output.append(lastElement)
        } else {
            output.append(lines)
            output.append(remainder)
        }
        
        return output
    }
}

let widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
let S = "bbbcccdddaaa"

let solution = Solution()
solution.numberOfLines(widths, S)

