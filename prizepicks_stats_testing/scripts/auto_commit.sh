current_date=$(date +"%m-%d-%Y")
repo_dir="$(cd "$(dirname "$(dirname "$(dirname "$(realpath "${BASH_SOURCE[0]}")")")")" && pwd)"

git add repo_dir
git commit -m "auto committing data for $current_date"
git push
