#!/bin/bash

# Check if a day number is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 day-number [year]"
    exit 1
fi

# Format the day number to two digits (e.g., 1 becomes 01)
DAY=$(printf "%02d" $1)

# Set the year, default to current year if not provided
YEAR=${2:-$(date +%Y)}

# Define file paths using the formatted day number and year
BASE_DIR=$(pwd)
PYTHON_FILE="$BASE_DIR/$YEAR/Python/$DAY.py"
INPUTS_FILE="$BASE_DIR/data/$YEAR/inputs/$DAY.txt"
PUZZLES_FILE="$BASE_DIR/data/$YEAR/puzzles/$DAY.md"

# Check if the files exist
if [ ! -f "$PYTHON_FILE" ] || [ ! -f "$INPUTS_FILE" ] || [ ! -f "$PUZZLES_FILE" ]; then
    echo "One or more files do not exist for day $DAY of year $YEAR"
    exit 1
fi

# Open files in Visual Studio Code side-by-side
code -r $PUZZLES_FILE -g $PUZZLES_FILE:1:1
code -r $INPUTS_FILE -g $INPUTS_FILE:1:1
code -r $PYTHON_FILE -g $PYTHON_FILE:1:1
