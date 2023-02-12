from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str,
                    default="./data/jogging.csv", help="ファイル名")
parser.add_argument("--output", type=str,
                    default="./output/hill-jogging.png", help="出力画像ファイル名")
parser.add_argument("--start_year", type=int,
                    default=2022, help="開始年")
parser.add_argument("--end_year", type=int,
                    default=2023, help="開始年")
                    

def main():
    args = parser.parse_args()
    data = pd.read_csv(args.data, index_col=0, parse_dates=True)
    data.sort_index(inplace=True)
    data.index = pd.to_datetime(data.index)

    now = args.start_year
    years = list(range(args.start_year, args.end_year + 1))
    dflist= [data.loc[f"{now}"] for now in years]


    f = plt.figure(figsize=(5, 5))
    a = f.gca()
    a.grid(lw=0.5, ls="--")
    for (i, yi) in enumerate(years):
        dfi = dflist[i]
        x = [(d - datetime(d.year, 1, 1)).days for d in dfi.index.tolist()]
        y = dfi.km.tolist()
        yc = np.cumsum(y)
        a.plot(x, yc, ms=2, marker="o", label=yi)
        
    a.set_xlabel("[days]")
    a.set_ylabel("[km]")
    a.legend()
    plt.tight_layout()
    plt.savefig(args.output)
    plt.close()



if __name__ == '__main__':
    main()
