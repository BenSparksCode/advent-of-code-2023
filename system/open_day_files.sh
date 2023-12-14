#!/bin/bash

# Check if a day number is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 day-number"
    exit 1
fi

# Format the day number to two digits (e.g., 1 becomes 01)
DAY=$(printf "%02d" $1)

# Define file paths using the formatted day number
PYTHON_FILE="src/bin/$DAY.py"
INPUTS_FILE="data/inputs/$DAY.txt"
PUZZLES_FILE="data/puzzles/$DAY.md"

# Check if the files exist
if [ ! -f "$PYTHON_FILE" ] || [ ! -f "$INPUTS_FILE" ] || [ ! -f "$PUZZLES_FILE" ]; then
    echo "One or more files do not exist for day $DAY"
    exit 1
fi

# Open files in Visual Studio Code side-by-side
code -r $PUZZLES_FILE -g $PUZZLES_FILE:1:1
code -r $INPUTS_FILE -g $INPUTS_FILE:1:1
code -r $PYTHON_FILE -g $PYTHON_FILE:1:1
