#!/bin/bash

input_file="$1"

output_file="$2"

if [ -f $output_file ]; then
    rm "$output_file"
fi

first_line=true
sequence=""

while IFS= read -r line || [[ -n $line ]]
do
    if [[ $line == \>* ]]; then
        if [ "$first_line" = false ]; then
            echo "$sequence" >> "$output_file"
            echo "" >> "$output_file"
        fi

        echo "$line" >> "$output_file"
        sequence=""
        first_line=false
    else
        sequence+="${line//-/}"
    fi
done < "$input_file"

if [ -n "$sequence" ]; then
    echo "$sequence" >> "$output_file"
fi

echo "" >> "$output_file"
