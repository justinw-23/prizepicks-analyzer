#!/bin/bash

export TZ="America/Los_Angeles"
current_date=$(date +"%Y-%m-%d")
current_date_snake_case=$(date +"%Y_%m_%d")
current_month=$(date +"%B")
current_year=$(date +"%Y")
month="${current_month} ${current_year}"

scripts_dir="$(cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")" && pwd)"
core_dir="$(cd "$(dirname "$(dirname "$(realpath "${BASH_SOURCE[0]}")")")" && pwd)"

box_score_filename="${core_dir}/data/${month}/${current_date}-Data/nba_box_scores_${current_date_snake_case}.csv"
ftn_picks_filename="${core_dir}/data/${month}/${current_date}-Data/nba_ftn_picks_${current_date_snake_case}.csv"
pine_picks_filename="${core_dir}/data/${month}/${current_date}-Data/nba_pine_picks_${current_date_snake_case}.csv"
analyzed_filename="${core_dir}/data/${month}/${current_date}-Data/ftn_picks_analyzed_${current_date_snake_case}.csv"
pine_analyzed_filename="${core_dir}/data/${month}/${current_date}-Data/pine_picks_analyzed_${current_date_snake_case}.csv"
hits_filename="${core_dir}/data/hits.txt"

python3 "$scripts_dir/process_ftn_picks.py" "$box_score_filename" "$ftn_picks_filename" "$analyzed_filename"
python3 "$scripts_dir/count_ftn_hits.py" "$analyzed_filename" "$hits_filename"

# python3 "$scripts_dir/process_pine_picks.py" "$box_score_filename" "$pine_picks_filename" "$pine_analyzed_filename"
# python3 "$scripts_dir/count_pine_hits.py" "$pine_analyzed_filename" "$hits_filename"

