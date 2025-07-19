"use strict";

//find length of longest  substring without repeating letters
export function findLengthOfLSWR(str: string): number {
  //empty string condition
  if (str === "") return 0;
  //repeating 1 or more times letter string condition
  if (str.length === 1 || str.split("").every((ltr) => ltr === str[0]))
    return 1;
  let result = 2;
  for (let start = 0, end = start + result; end <= str.length; end++) {
    const partialStr = str.substring(start, end);
    const unique = validateUniqueString(partialStr);
    if (unique) {
      //update result
      result = end - start;
    } else {
      //move start index forward
      start++;
    }
  }
  return result;
}
export function validateUniqueString(str: string): boolean {
  //! Assuming capital letters cannot replace lowercase ones
  return [...new Set(str.split(""))].length === str.length;
}
