from datetime import datetime
import calmap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str,
                    default="./data/power-training.csv", help="ファイル名")
parser.add_argument("--output", type=str,
                    default="./output/power-training.png", help="出力画像ファイル名")
parser.add_argument("--start", type=str,
                    default="2022-1-1", help="開始日")
parser.add_argument("--end", type=str,
                    default="2022-12-31", help="終了日")
parser.add_argument("--single", action="store_true", help="1列目だけ読むかどうか")


def main():
    args = parser.parse_args()
    print(args)

    if args.single:
        data = pd.read_csv(args.data, index_col=0, parse_dates=True)
        events = pd.Series(np.ones(data.shape[0]), index=data.index)
    else:
        data = pd.read_csv(args.data, index_col=0, parse_dates=True)
        events = data.km

    date_start = datetime.strptime(args.start, "%Y-%m-%d")

    if args.single:
        calmap.yearplot(events, year=date_start.year, daylabels="MTWTFSS",
                        fillcolor="grey", linewidth=0.1, vmin=0, vmax=1)
    else:
        calmap.yearplot(events, year=date_start.year, daylabels="MTWTFSS",
                        fillcolor="grey", linewidth=0.1)

    plt.tight_layout()
    plt.savefig(args.output, bbox_inches="tight")
    plt.close()


if __name__ == '__main__':
    main()
