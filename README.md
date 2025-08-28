# TDD Driven StringCalculator

Build a StringCalculator functionality that can take up to two numbers, separated by commas, and will return their sum. 
for example “” or “1” or “1,2” as inputs.

> DO NOT jump into implementation! Read the example and the starting task below.

- For an empty string it will return 0
- Allow the Add method to handle an unknown amount of numbers
- Allow the Add method to handle new lines between numbers (instead of commas).
  - the following input is ok: “1\n2,3” (will equal 6)
  - the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)
- Support different delimiters : to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
the first line is optional. all existing scenarios should still be supported
- Calling Method with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. if there are multiple negatives, show all of them in the exception message.
- Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
- Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6

## Tasks



Establish quality parameters:

- Ensure  maximum complexity (CCN) per function == 3

- Ensure 100% line and branch coverage at every step

  

Start Test-driven approach

1. Write the smallest possible failing test: give input `"" assert output to be 0 ` .
2. Write the minimum amount of code that'll make it pass.
3. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.
# StringCalculator






A simple **String Calculator** implemented in Python following **Test-Driven Development (TDD)** principles.

---

## Features

- Returns the sum of numbers given in a string input.
- Supports:
  - Empty string input (returns 0).
  - An unknown amount of numbers.
  - Comma `,` and newline `\n` as default delimiters.
  - Custom delimiters specified in the format:  
    `//[delimiter]\n[numbers…]`  
    e.g. `"//;\n1;2"` returns `3`.
  - Custom delimiters of any length using square brackets:  
    e.g. `"//[***]\n1***2***3"` returns `6`.
  - Multiple custom delimiters:  
    e.g. `"//[*][%]\n1*2%3"` returns `6`.
  - Throws an exception if negative numbers are included, listing all negatives.
  - Ignores numbers greater than 1000.

---
   
