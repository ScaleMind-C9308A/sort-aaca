# SORT-AACA - Sorting Algorithms: A Comparative Analysis

<p style="text-align:justify"> SORT-AACA is a shorterm project conducting the experiment of comparing the performance of the two modenest sorting algorithm: Timsort and IntroSort. The project provides friendly CLI command to conduct the experiment in different scenarios including changing the hyperparameters of the sorting algorithm, conguring the description of the list used in testing, or switching the backbone used in each algorithm. </p>

# Setup
## Clone
### Local
```
git clone https://github.com/KhoiDOO/sort-aaca.git
```

### GoogleColab
```
!git clone https://github.com/KhoiDOO/sort-aaca.git
```

## Env
### Window
```
cd sort-aaca
python -m venv .env
.env\Script\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

```

### Linux System
```
python3.x -m venv .env
source .env/bin.activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

# Experiment
## CLI help
```
python main.py -h, --help
```

## Run
### Local
```
python main.py --min_size 10 --max_size 1000 --negative --fig_size [25, 15] --font_scale 2 --tim_min_merge 32 --intro_min_size 16
```

### Google Colab
```
cd sort-aaca
!python main.py --min_size 10 --max_size 1000 --negative --fig_size [25, 15] --font_scale 2 --tim_min_merge 32 --intro_min_size 16
```

# Result

