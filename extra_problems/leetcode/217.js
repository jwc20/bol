/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  nums.sort();
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === nums[i+1]) {
      return true;
    }
  }
  return false;
};

nums1 = [1, 2, 3, 1];
nums2 = [1, 2, 3, 4];
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2];
nums4 = [2,14,18,22,22];

console.log(
  containsDuplicate(nums1),
  containsDuplicate(nums2),
  containsDuplicate(nums3),
  containsDuplicate(nums4)
); // => true, false, true, true
