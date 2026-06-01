# FIFA-2019-Player-Data-Analysis
A exploratory data analysis (EDA) project built with Python that dives into the FIFA 2019 player dataset, uncovering patterns and insights through a rich set of visualizations.
Value Parsing — Cleans and converts player market values from string format (e.g. €100M, €500K) into numeric figures for analysis
Age Distribution — Visualizes player age spread using histograms and KDE plots
Preferred Foot Analysis — Explores foot preference distributions via count plots, pie charts, and bar charts; compares average player value by foot
Position & Foot Breakdown — Cross-analyzes player positions with preferred foot using count plots and boxplots
International Reputation vs Potential — Examines the relationship between reputation levels and player potential through scatter plots, strip plots, and boxplots
Potential vs Overall Rating — Investigates how potential correlates with current overall rating using line and scatter plots
Combined Dashboard — A 2×2 subplot grid summarizing the key relationships in a single view


🛠️ Tech Stack
LibraryPurposepandasData loading and manipulationnumpyNumerical operationsmatplotlibPlot renderingseabornStatistical visualizations

🚀 Getting Started
bashpip install pandas numpy matplotlib seaborn
Update the dataset path in the script:
pythondf = pd.read_csv("path/to/Fifa 2019.csv")
Then run:
bashpython Fifa_Lahiye.py

📁 Dataset
https://www.kaggle.com/datasets/karangadiya/fifa19
