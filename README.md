# Python Learning Journey

A documented journey of learning Python from fundamentals to practical programming through daily coding exercises, problem-solving, and hands-on implementation.

## Introduction

This repository documents my journey of learning Python from scratch. I am a beginner, and the code here shows what I have studied so far at my current level of understanding.

The repository contains:

- Daily Python exercises
- Programming fundamentals
- Practical implementations
- Problem-solving practice
- Learning progress and milestones

## Learning Objectives

- Develop strong Python fundamentals.
- Understand programming logic.
- Improve problem-solving ability.
- Practise writing clean and readable code.
- Progress towards intermediate and advanced Python.
- Build practical projects after establishing fundamentals.

## Learning Progress Tracker

| Day | Topics | Status |
|---|---|---|
| [Day 01](Day-01/) | Strings, concatenation, length, indexing, slicing, conditional statements | Completed |
| Day 02 | To be updated | Not started |

## Repository Structure

```text
Python-Learning-Journey/
├── README.md
├── .gitignore
└── Day-01/
    ├── Day1.py
    └── Day1_QP.py
```

- **`Day-XX/` folders**: each day of learning has its own folder, for example `Day-01/`. A new folder is added only when that day has real learning material.
- **`DayN.py` files**: notes and examples of the concepts studied that day.
- **`DayN_QP.py` files**: practice questions (QP) solved that day.

### Running the programs

The programs need Python 3. Run them from the repository root:

```bash
python3 Day-01/Day1.py
python3 Day-01/Day1_QP.py
```

`Day1_QP.py` is interactive. It asks for input in the terminal, and the number prompts expect whole numbers.

## Concepts Covered

These lists show the concepts I practised in each day's files. Practising a concept is not the same as mastering it, and I expect to come back to these topics.

### Day 01

**Strings**

- Creating string variables
- Finding the length of a string with `len()`
- Joining strings with the `+` operator (concatenation)
- Getting a single character by its index, for example `string[0]`
- Slicing a range of characters with `string[start:end]`
- Slicing with the start or end index left out, for example `string[0:]` and `string[:4]`
- Using `len()` as the end index of a slice
- Counting how many times a character appears with `.count()`

**Input and type conversion**

- Reading user input with `input()`
- Converting input text to a whole number with `int()`

**Conditional statements**

- `if` / `else` for a choice between two outcomes
- `if` / `elif` / `else` for a choice between more than two outcomes
- Comparison operators `==` and `>=`
- Combining two conditions with `and`
- Using the remainder operator `%` to check divisibility (even/odd and multiple of 7)

## Practice Exercises

### Day 01

[`Day1.py`](Day-01/Day1.py): string basics

1. Find the length of two strings, join them with a space, and print the result and its length.
2. Print the first character of a string using indexing.
3. Print the whole string and part of the string using slicing.

[`Day1_QP.py`](Day-01/Day1_QP.py): practice questions

1. Ask for the user's first name and print its length.
2. Count how many times `$` appears in a string.
3. Check whether a number entered by the user is even or odd.
4. Find the greatest of three numbers entered by the user.
5. Check whether a number is a multiple of 7.

## Future Learning Roadmap

These are planned learning goals, not completed achievements. The tracker above records actual progress.

1. Python fundamentals
2. Variables and data types
3. Operators and expressions
4. Conditional statements
5. Loops
6. Strings
7. Lists and tuples
8. Dictionaries and sets
9. Functions
10. File handling
11. Object-oriented programming
12. Modules and packages
13. Exception handling
14. Problem-solving and practical projects

Strings and conditional statements were introduced on Day 01. They stay on the roadmap because there is much more to learn about both.

## Progress Philosophy

This repository puts consistent learning, genuine implementation, and gradual improvement ahead of a perfect commit streak. I add work when I have actually studied and practised something. Some days will have more material than others, and some topics will take more than one day.

## Disclaimer

This is an ongoing educational repository. The code reflects my understanding at different stages of learning, so early exercises are simple and may not follow every best practice. They are kept close to how I first wrote them so that my progress stays visible.

Before publishing, the Day 01 files received small readability edits: spacing, comment spelling, descriptive names for two variables, and clearer output messages. The logic and the approach of each exercise did not change.
