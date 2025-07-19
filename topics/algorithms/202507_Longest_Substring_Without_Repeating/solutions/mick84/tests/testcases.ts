export type Case = [string, number];
export const testCases: Case[] = [
  ["", 0],
  ["aaaaa", 1],
  ["XXXL", 2],
  ["longstring", 8],
  [" longstriNG", 11],
  ["abcdevaqdcbzdv", 8],
];
