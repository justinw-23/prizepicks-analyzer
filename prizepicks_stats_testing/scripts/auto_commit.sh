current_date=$(date +"%m-%d-%Y")
cd "$(dirname "$(dirname "$(dirname "$(realpath "${BASH_SOURCE[0]}")")")")"

git add .
git commit -m "auto committing data for $current_date"
git push
