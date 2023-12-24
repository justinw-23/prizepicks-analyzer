import csv
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()

    parser.add_argument('box_score_filename', type=str)
    parser.add_argument('pine_picks_filename', type=str)
    parser.add_argument('output_filename', type=str)

    args = parser.parse_args()

    bsfpath = args.box_score_filename
    box_score_dict = dict()
    try:
        with open(bsfpath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
            if header is None:
                print("Box scores CSV file is empty.")
                return
            for row in reader:
                name = row[1]
                box_score_dict[name] = row
    except FileNotFoundError:
        print(f"The file bsfpath '{bsfpath}' was not found.")
    except Exception as e:
        print(f"Error arg 1 occurred: {e}")

    pine_picks_path = args.pine_picks_filename
    output_file = args.output_filename
    try:
        with open(pine_picks_path, 'r', newline='', encoding='utf-8') as csvfile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(outfile)

            header = next(reader, None)
            if header is None:
                print("Pine picks CSV file is empty.")
                return
            else:
                header.append("Result")
                writer.writerow(header)
            for row in reader:
                print(row)
                if row[0] == "Game":
                    print("Reached duplicate header, aborting...")
                    return # duplicate data was appended to the csv file
                hit = False
                category = row[2]
                line = float(row[3])
                bet = row[9]
                if bet.upper() != "OVER" and bet.upper() != "UNDER":
                    continue
                if row[1] in box_score_dict:
                    player_stats = box_score_dict[row[1]]
                else:
                    continue
                threes = int(player_stats[6].split('-')[0])
                rebounds = int(player_stats[11])
                assists = int(player_stats[12])
                steals = int(player_stats[14])
                blocks = int(player_stats[15])
                turnovers = int(player_stats[16])
                points = int(player_stats[17])
                #,1Player,2Status,3Pos,4Min,5FGM-A,63PM-A,7FTM-A,8FIC,9Off,10Def,11Reb,12Ast,13PF,14STL,15BLK,16TO,17PTS

                total = None
                if category == "PA":
                    total = points + assists
                elif category == "RA":
                    total = rebounds + assists
                elif category == "PAR":
                    total = points + rebounds + assists
                elif category == "Rebounds":
                    total = rebounds
                elif category == "PR":
                    total = points + rebounds
                elif category == "Points":
                    total = points
                elif category == "Blocks":
                    total = blocks
                elif category == "Turnovers":
                    total = turnovers
                elif category == "Three Points Made":
                    total = threes
                elif category == "SB":
                    total = blocks + steals
                elif category == "Assists":
                    total = assists
                elif category == "Steals":
                    total = steals
                elif category == "Fantasy Points - PrizePicks":
                    total = 3*blocks + 3*steals + 1.5*assists + 1.2*rebounds + points - turnovers
                else:
                    continue

                if total > line:
                    if bet.upper() == "OVER":
                        hit = True
                elif total < line:
                    if bet.upper() == "UNDER":
                        hit = True
                if hit:
                    row.append("Hit")
                else:
                    row.append("Miss")
                writer.writerow(row)
    except FileNotFoundError:
        print(f"The file pine_picks_path '{pine_picks_path}' was not found.")
    except Exception as e:
        print(f"Error arg 2 occurred: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(2)
