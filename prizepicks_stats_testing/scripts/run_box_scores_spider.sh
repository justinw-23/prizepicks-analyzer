#!/bin/bash

export TZ="America/Los_Angeles"
current_date=$(date +"%Y-%m-%d")
current_date_snake_case=$(date +"%Y_%m_%d")
current_month=$(date +"%B")
current_year=$(date +"%Y")
month="${current_month} ${current_year}"

output_path="$(realpath ..)/data/${month}/${current_date}-Data/nba_box_scores_${current_date_snake_case}.csv"
venv_path="$(realpath ../..)/venv/bin/activate"

source "$venv_path"

scrapy crawl box_scores_spider -o "$output_path"

deactivate
