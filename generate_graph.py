import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d


def generate_graph(filename="data.csv"):
    LEETCODE_YELLOW = "#ffa115"
    df = pd.read_csv(filename)
    print(df)
    df["points"] = df["points"].astype(float)
    x0 = range(len(df))
    y0 = df["points"].tolist()
    plt.figure(facecolor="#282828")
    plt.rcParams["text.color"] = LEETCODE_YELLOW
    plt.rcParams["axes.labelcolor"] = LEETCODE_YELLOW
    plt.rcParams["xtick.color"] = LEETCODE_YELLOW
    plt.rcParams["ytick.color"] = LEETCODE_YELLOW
    marker_size = 2 if len(df) < 10 else 1
    plt.plot(x0, y0, "o", color="#ffa115", markersize=marker_size)
    cubic_interpolation_model = interp1d(x0, y0, kind="cubic")
    x = np.linspace(min(x0), max(x0), 5000)
    y = cubic_interpolation_model(x)
    plt.plot(x, y, color="#ffa115")
    plt.box(False)
    plt.tick_params(
        axis="x",
        which="both",
        bottom=False,
        top=False,
        labelbottom=False,
    )

    plt.yticks(np.arange(min(y0) // 250 * 250 - 250, max(y0) + 250, 250))
    plt.savefig("points_graph.png", bbox_inches="tight", dpi=300)
    return


if __name__ == "__main__":
    generate_graph()
