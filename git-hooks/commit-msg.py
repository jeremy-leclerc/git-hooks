#!/bin/bash

commit_msg_file="$1"
commit_msg=$(cat "$commit_msg_file")

# Debugging echo statements
echo "Commit message file: $commit_msg_file"
echo "Commit message: $commit_msg"

# Define regex pattern for commit message format
pattern="^\[#\d+\] .+"

# Check if commit message matches the pattern
if [[ $commit_msg =~ $pattern ]]; then
    echo "Commit message format is correct."
else
    echo "Error: Commit message format is incorrect. It should be in the format '[#1234] commit message after the numbers'."
    exit 1
fi