#!/bin/bash

current_date=$(date +"%Y-%m-%d")
current_date_snake_case=$(date +"%Y_%m_%d")
process_csv_path="./process_csv_files.py"
count_hits_path="./count_hits.py"
box_score_filename="../data/${current_date}-data/nba_box_scores_${current_date_snake_case}.csv"
edge_picks_filename="../data/${current_date}-data/nba_edge_picks_${current_date_snake_case}.csv"
output_filename="../data/${current_date}-data/edge_picks_analyzed_${current_date_snake_case}.csv"

python3 "$process_csv_path" "$box_score_filename" "$edge_picks_filename" "$output_filename"
python3 "$count_hits_path" "$output_filename"
