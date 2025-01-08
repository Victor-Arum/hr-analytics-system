This project is designed to analyze, retrieve, visualize, and interact with Human Resource (HR) metrics. 
It includes tools for processing HR data, analyzing key performance indicators, and presenting insights through an interactive text-based user interface (TUI) and visualizations.

## How To Use the Repository
- Run retrieve.py or retrieve.ipynb to load and preprocess the HR data.
- Run analyse.py or analyse.ipynb for in-depth analysis of HR metrics.
- Run visualise.py or visualise.ipynb to generate visual insights.
- Run tui.py or test its functionality in tui.ipynb to interact with the project.
- Finally, run main.py to execute the entire workflow interactively.

## Python Files

- retrieve.py
A script for retrieving and preprocessing HR data.
Handles operations like data loading, filtering, and structuring for further analysis.
Outputs: Processed datasets ready for analysis and visualization.

- analyse.py
Implements core analytical functions for HR metrics.
Includes statistical summaries and key performance indicator (KPI) calculations.
Outputs: Insights like employee retention rates, performance distributions, and trends.

- visualise.py
A script for visualizing HR data through charts and graphs.
Uses libraries like Matplotlib or Seaborn to create visual summaries of trends and metrics.
Outputs: Visualizations such as bar charts, line plots, and heatmaps.

- tui.py
A Text-Based User Interface (TUI) for interacting with the project.
Allows users to retrieve, analyze, and visualize data directly through command-line inputs.
Outputs: Interactive terminal-based outputs and prompts for user commands.

## Jupyter Notebooks

- retrieve.ipynb
A notebook version of the retrieve.py script.
Provides step-by-step data retrieval and preprocessing for easier comprehension.
Outputs: Cleaned and structured datasets for downstream tasks.

- analyse.ipynb
A notebook for performing HR data analysis interactively.
Includes examples and visual outputs for key metrics and insights.
Outputs: KPI analysis, trends, and exploratory visualizations.

- visualise.ipynb
Interactive notebook for generating and customizing HR data visualizations.
Outputs: Graphical representations of metrics and trends.

- tui.ipynb
Notebook implementation of the Text-Based User Interface.
Allows testing and demonstration of the TUI functionalities.

- main.ipynb
Integrates all the modules (retrieve, analyse, visualise, tui) into a cohesive workflow.
Serves as a central point for executing the project pipeline interactively.
Outputs: Combined outputs of data retrieval, analysis, and visualization.

## Dataset

- HR_Metrics.csv
The dataset containing HR metrics for analysis.
Includes features like employee demographics, job roles, performance metrics, and retention details.
Basis for all analysis and visualization tasks in the project.
