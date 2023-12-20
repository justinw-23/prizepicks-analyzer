#!/bin/bash

# Get the directory of the script
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Define patterns and corresponding new cron commands
patterns=("run_edge_spider.sh" 
          "run_box_scores_spider.sh"
          "run_analysis.sh")
new_commands=("45 12 * * * $script_dir/scripts/run_edge_spider.sh"
              "45 22 * * * $script_dir/scripts/run_box_scores_spider.sh"
              "47 23 * * * $script_dir/scripts/run_analysis.sh")

# Check if matching cron jobs are present and replace them with the corresponding new cron commands
existing_cron_jobs=$(crontab -l | grep -E "$(IFS=\|; echo "${patterns[*]}")")

if [ "$existing_cron_jobs" ]; then
    # Remove existing cron jobs that match any of the patterns and add the new cron commands
    (crontab -l | grep -vE "$(IFS=\|; echo "${patterns[*]}")"; printf "%s\n" "${new_commands[@]}") | crontab -
else
    # If no matching cron jobs, add the new cron commands
    (crontab -l ; printf "%s\n" "${new_commands[@]}") | crontab -
fi

echo "Cron tasks generated successfully. View your tasks with 'crontab -l'."
