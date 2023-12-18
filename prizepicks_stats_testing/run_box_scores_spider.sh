#!/bin/bash

current_date=$(date +"%Y-%m-%d")
current_date_snake_case=$(date +"%Y_%m_%d")
output_path="/Users/justin/Desktop/prizepicks_stats_testing/prizepicks_stats_testing/${current_date}-data/nba_box_scores_${current_date_snake_case}.csv"

cd /Users/justin/Desktop/prizepicks_stats_testing/prizepicks_stats_testing

source /Users/justin/Desktop/prizepicks_stats_testing/prizepicks_stats_testing/venv/bin/activate

scrapy crawl box_scores_spider -o "$output_path"

deactivate
