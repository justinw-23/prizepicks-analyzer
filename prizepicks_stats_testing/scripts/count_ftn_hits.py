import csv
import sys
from datetime import datetime

def main():
    formatted_date = datetime.now().strftime("%m/%d/%y")
    total = 0
    total_over_60 = 0
    hits = 0
    hits_over_60 = 0
    fpath = sys.argv[1]
    with open(fpath, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)
        if header is None:
            print("FTN picks analyzed CSV file is empty.")
            return
        for row in reader:
            if row[6] == "Hit":
                hits += 1
            total += 1
            if float(row[5].strip("%")) >= 60.0:
                if row[6] == "Hit":
                    hits_over_60 += 1
                total_over_60 += 1
    
    outpath = sys.argv[2]
    with open(outpath, "a") as outfile:
        outfile.write(f"FTN Hits/Total for {formatted_date}: {hits}/{total}\n")
        outfile.write(f"\tFTN Hits/Total for {formatted_date} over 60.0%: {hits_over_60}/{total_over_60}\n")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(2)
