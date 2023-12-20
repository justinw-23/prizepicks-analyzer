#!/bin/bash

current_date=$(date +"%Y-%m-%d")
current_date_snake_case=$(date +"%Y_%m_%d")
output_path="/Users/justin/dev/prizepicks-analyzer/prizepicks_stats_testing/data/${current_date}-data/nba_edge_picks_${current_date_snake_case}.csv"

cd /Users/justin/dev/prizepicks-analyzer

source /Users/justin/dev/prizepicks-analyzer/venv/bin/activate

scrapy crawl edge_picks_spider -o "$output_path"

deactivate