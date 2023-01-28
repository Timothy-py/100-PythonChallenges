// Given an integer array nums, find the subarray with the largest sum, and return its sum.
// Subarray: A subarray is a contiguous non-empty sequence of elements within an array.

function maxSubArray(arr) {
    let maxEndingHere = arr[0], maxSoFar = arr[0]
    for (let i=1; i < arr.length; i++) {
        maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i])
        maxSoFar = Math.max(maxSoFar, maxEndingHere)
    }
    return maxSoFar
}


let arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
console.log(maxSubArray(arr)); // Output: 6
