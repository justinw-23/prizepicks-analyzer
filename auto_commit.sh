current_date=$(date +"%m-%d-%Y")
repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

git add .
git commit -m "auto committing data for $current_date"
git push
