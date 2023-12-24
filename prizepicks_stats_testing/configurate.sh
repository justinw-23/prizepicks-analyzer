#!/bin/bash

# Get the directory of the script
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Define patterns and corresponding new cron commands
patterns=("run_ftn_picks_spider.sh" 
          "run_box_scores_spider.sh"
          "run_analysis.sh")
new_commands=("59 12 * * * /bin/bash $script_dir/scripts/run_ftn_picks_spider.sh >> /home/ubuntu/crontest.log 2>&1"
              "45 22 * * * /bin/bash $script_dir/scripts/run_box_scores_spider.sh >> /home/ubuntu/crontest.log 2>&1"
              "47 22 * * * /bin/bash $script_dir/scripts/run_analysis.sh >> /home/ubuntu/crontest.log 2>&1")

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
