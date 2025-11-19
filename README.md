# Zomato Data Analysis

**A clear, reproducible Exploratory Data Analysis (EDA) project on Zomato restaurant data.**
This repository contains a clean EDA script, sample dataset, visualizations, and insights aimed to demonstrate data cleaning, feature engineering, visualization and storytelling with Python.

## 🚀 Highlights
- Data cleaning and preprocessing of messy datasets
- EDA using Pandas and Matplotlib / Seaborn
- Visualizations showing rating distribution, top cuisines, and correlations
- Reproducible Jupyter-ready workflow

## Contents
- `zomato_analysis.py` - a runnable Python script demonstrating EDA steps.
- `zomato_dataset.csv` - a small sample dataset to test the scripts.
- `README.md` - this file.
- `notebooks/` (suggested) - Jupyter notebooks for interactive analysis (optional).

## Setup / Run
1. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
```
2. Run the analysis script:
```bash
python zomato_analysis.py
```
3. Check generated plots: `rating_plot.png` and other saved figures.

## Example Analysis Steps (in `zomato_analysis.py`)
- Load dataset and inspect missing values
- Clean/normalize columns (cost, rating formats)
- Group by cuisine / city for aggregated insights
- Visualize rating distribution and cuisine popularity

## Dataset
Use a public Zomato dataset (Kaggle) for full analysis. The included `zomato_dataset.csv` is a small placeholder to demonstrate the script.

## Results & Insights
- Typical insights include distribution of ratings, most popular cuisines, and correlation between votes and rating.
- Save final figures and a short conclusions section for the README.

## License
MIT © Your Name