import csv
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()

    parser.add_argument('box_score_filename', type=str)
    parser.add_argument('edge_picks_filename', type=str)
    parser.add_argument('output_filename', type=str)

    args = parser.parse_args()

    bsfpath = args.box_score_filename
    bsdict = dict()
    try:
        with open(bsfpath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                bsdict[row[1]] = row
                #print(row)
    except FileNotFoundError:
        print(f"The file bsfpath '{bsfpath}' was not found.")
    except Exception as e:
        print(f"An error occurdfdgdsgfdred: {e}")

    eppath = args.edge_picks_filename
    output_file = args.output_filename
    try:
        with open(eppath, 'r', newline='', encoding='utf-8') as csvfile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(outfile)

            header = next(reader)
            for row in reader:
                hit = False
                category = row[2]
                line = float(row[3])
                bet = row[4]
                if row[0] in bsdict:
                    player_stats = bsdict[row[0]]
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
                if category == "Pts+Asts":
                    total = points + assists
                elif category == "Rebs+Asts":
                    total = rebounds + assists
                elif category == "Pts+Rebs+Asts":
                    total = points + rebounds + assists
                elif category == "Rebounds":
                    total = rebounds
                elif category == "Pts+Rebs":
                    total = points + rebounds
                elif category == "Points":
                    total = points
                elif category == "Blocked Shots":
                    total = blocks
                elif category == "Turnovers":
                    total = turnovers
                elif category == "3-PT Made":
                    total = threes
                elif category == "Blks+Stls":
                    total = blocks + steals
                elif category == "Assists":
                    total = assists
                elif category == "Steals":
                    total = steals
                elif category == "Fantasy Score":
                    total = 3*blocks + 3*steals + 1.5*assists + 1.2*rebounds + points - turnovers
                else:
                    continue

                if total > line:
                    if bet == "OVER":
                        hit = True
                elif total < line:
                    if bet == "UNDER":
                        hit = True
                if hit:
                    row.append("Hit")
                else:
                    row.append("Miss")
                writer.writerow(row)
    except FileNotFoundError:
        print(f"The file eppath '{eppath}' was not found.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(2)
