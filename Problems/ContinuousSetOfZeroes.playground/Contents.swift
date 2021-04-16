
import Foundation

// Implement a function that takes an array that contains any number of 1s and 0s, and returns true if there is exactly one continuous set of zeros.

// For example [0,0,1,1] should return true, [1,0,0,0,0,1,0] should return false. 4


func continuousSetOfZeroes(_ input:[Int]) -> Bool {
    
    var arr = [Int]()
    var tcount = 0
    
    for i in input {
        if i == 0 {
            arr.append(i)
            if arr.count > 1 && arr.count < 3 {
                tcount += 1
            }
        } else {
            arr.removeAll()
        }
    }
    print("Total consecutive zeroes:", tcount)
    return tcount == 1 ? true: false
}
  
let x = continuousSetOfZeroes([0, 0, 3, 0])
print(x)
