# Toy Programming Language Compiler

### Compiler Design | Assignment 3 | Semester VII

## Objective
This project implements a basic compiler for a toy programming language. The language supports variable assignments, arithmetic operations, and conditional statements. The compiler consists of three main components: a lexer, a parser, and an interpreter, which work together to evaluate and execute programs written in this toy language.

## Table of Contents
- [Language Features](#language-features)
- [Project Structure](#project-structure)
- [Grammar Definition](#grammar-definition)
- [Components](#components)
  - [Lexer](#lexer-lexerpy)
  - [Parser](#parser-parserpy)
  - [Interpreter](#interpreter-interpreterpy)
- [How to Run](#how-to-run)
- [Example Program](#example-program)
- [Error Handling](#error-handling)
- [Conclusion](#conclusion)
- [Future Improvements](#future-improvements)

## Language Features
This toy programming language includes the following features:

- **Variable Assignment**: You can assign values to variables, e.g., `x = 5;`.
- **Basic Arithmetic Operations**: The language supports addition, subtraction, multiplication, and division, e.g., `x = 5 + 3;`.
- **Conditional Statements**: The language supports basic conditional expressions using `if` and `then` statements, e.g., `if x == 5 then y = 10;`.
- **Whitespace Insensitivity**: The language ignores spaces and tabs, making it flexible in terms of formatting.

## Project Structure
The project consists of the following files:
- **lexer.py**: Handles lexical analysis (tokenizing the source code).
- **parser.py**: Handles parsing (building an abstract syntax tree from tokens).
- **interpreter.py**: Handles interpretation (evaluating and executing the abstract syntax tree).
- **main.py**: Combines all components and runs the toy language.

## Grammar Definition
The grammar for the toy language includes the following rules:

```ebnf
statement   -> "if" condition "then" statement | assignment
assignment  -> IDENTIFIER "=" expression
expression  -> term (("+" | "-") term)*
term        -> factor (("*" | "/") factor)*
factor      -> NUMBER | IDENTIFIER | "(" expression ")"
condition   -> expression ("==" | "!=" | "<" | ">" | "<=" | ">=") expression
