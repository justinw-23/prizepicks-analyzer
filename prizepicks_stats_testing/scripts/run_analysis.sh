#!/bin/bash

export TZ="America/Los_Angeles"
current_date=$(date +"%Y-%m-%d")
current_date_snake_case=$(date +"%Y_%m_%d")
current_month=$(date +"%B")
current_year=$(date +"%Y")
month="${current_month} ${current_year}"

box_score_filename="$(realpath ..)/data/${month}/${current_date}-Data/nba_box_scores_${current_date_snake_case}.csv"
edge_picks_filename="$(realpath ..)/data/${month}/${current_date}-Data/nba_edge_picks_${current_date_snake_case}.csv"
analyzed_filename="$(realpath ..)/data/${month}/${current_date}-Data/edge_picks_analyzed_${current_date_snake_case}.csv"
hits_filename="$(realpath ..)/data/hits.txt"

python3 process_csv_files.py "$box_score_filename" "$edge_picks_filename" "$analyzed_filename"
python3 count_hits.py "$analyzed_filename" "$hits_filename"
