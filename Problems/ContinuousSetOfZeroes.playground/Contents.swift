
import Foundation

// Return true if there are more than 1 set of continuous zeroes.

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
