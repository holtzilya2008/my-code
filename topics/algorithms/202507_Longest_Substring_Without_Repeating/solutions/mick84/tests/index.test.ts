import { findLengthOfLSWR, validateUniqueString } from "../index";
import { describe, expect, test } from "@jest/globals";
import { type Case, testCases } from "./testcases";
const testCallback = (applyFunc: Function, str: string, value: any) =>
  expect(applyFunc(str)).toBe(value);
const callback = ([input, output]: Case) =>
  test(
    `case '${input}', must return ${output}`,
    testCallback.bind(null, findLengthOfLSWR, input, output)
  );
describe("validateUniqueString unit tests", () => {
  test(
    "string hello! char l repeated, must return false",
    testCallback.bind(null, validateUniqueString, "hello", false)
  );
  test(
    "string hey! no repeated chars, must return true",
    testCallback.bind(null, validateUniqueString, "hey!", true)
  );
});
describe("findLengthOfLSWR unit tests", () => testCases.forEach(callback));
