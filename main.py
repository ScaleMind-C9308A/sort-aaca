import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import argparse
from tqdm import tqdm, trange
from datetime import datetime
import platform

from base.timsort import TimSort
from base.introsort import IntroSort

class Experiment:
    def __init__(self, args) -> None:
        self.args = args
        self.slash = "\\" if platform.system() == 'Window' else "/"
        self.log = {
            "Size" : [],
            "Timsort - Bubble" : [],
            "Timsort - Insertion" : [],
            "Timsort - Selection" : [],
            "Introsort - Bubble" : [],
            "Introsort - Insertion" : [],
            "Introsort - Selection" : []
        }

        self.result_dir = os.getcwd() + f"{self.slash}result"
        if not os.path.exists(self.result_dir):
            os.mkdir(self.result_dir)    

        self.tim_bub = TimSort(mode = "experiment", backbone = "bubble", min_merge=args.tim_min_merge)   
        self.tim_ins = TimSort(mode = "experiment", backbone = "insert", min_merge=args.tim_min_merge)   
        self.tim_sel = TimSort(mode = "experiment", backbone = "select", min_merge=args.tim_min_merge)   

        self.intro_bub = IntroSort(mode = "experiment", backbone = "bubble", min_size=args.intro_min_size)   
        self.intro_ins = IntroSort(mode = "experiment", backbone = "insert", min_size=args.intro_min_size)   
        self.intro_sel = IntroSort(mode = "experiment", backbone = "select", min_size=args.intro_min_size)   

    def experiment(self):
        for size in trange(self.args.min_size, self.args.max_size + 1):
            base_arr = self._random_lst(size=size)

            self.log["Size"].append(size)
            self.log["Timsort - Bubble"].append(self.tim_bub(base_arr))
            self.log["Timsort - Insertion"].append(self.tim_ins(base_arr))
            self.log["Timsort - Selection"].append(self.tim_sel(base_arr))

            self.log["Introsort - Bubble"].append(self.intro_bub(base_arr))
            self.log["Introsort - Insertion"].append(self.intro_ins(base_arr))
            self.log["Introsort - Selection"].append(self.intro_sel(base_arr))
        
        self._plot()

    def _random_lst(self, size: int) -> list:
        if self.args.negative:
            return np.random.randint(low = -1000, high=1000, size=size).tolist()
        else:
            return np.random.randint(low = 0, high=1000, size=size).tolist()

    def _plot(self):
        plt.figure(figsize=tuple(self.args.fig_size))
        sns.set(font_scale=self.args.font_scale)
        for key in self.log:
            if key != "Size":
                sns.lineplot(data = self.log, x = "Size", y = key, label = key)
        path = self.result_dir + f"/min_{self.args.min_size}_max_{self.args.max_size}_tim_min_{self.args.tim_min_merge}_intro_min_{self.args.intro_min_size}_neg_{self.args.negative}"
        plt.savefig(path)

    def _export_log(self, path):
        raise not NotImplementedError        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Sorting Algorithms: A Comparative Analysis',
                    description='This program conducts the experiment on the performance of Timsort, \
                        Introsort',
                    epilog='Enjoy!!!')
    
    parser.add_argument('--min_size', type=int, default=800,
                        help="max size of array in the experiment, this cannot be less than 10")
    parser.add_argument('--max_size', type=int, default=1000,
                        help="max size of array in the experiment, this cannot be less than 10 or min_size")
    parser.add_argument('--negative', action="store_true",
                        help="use negative number in the array")
    parser.add_argument('--fig_size', type=list, default=[25, 15],
                        help="Size of figure in Matplotlib")
    parser.add_argument('--font_scale', type=int, default=2,
                        help="Scale factor of font in plotting figure")
    
    parser.add_argument('--tim_min_merge', type=int, default=32,
                        help="The minimum number of elements in one block of the array, used in Timsort")
    parser.add_argument('--intro_min_size', type=int, default=16,
                        help="The minimum number of elements in one block of the array, used in Timsort")
    
    args = parser.parse_args()

    exp = Experiment(args=args)
    exp.experiment()
