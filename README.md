# F1 Analysis
Analyzing Formula 1 race data using Pandas and Matplotlib libraries, and SQL magic for IPython.


## Overview
Formula One (also Formula 1 or F1) is the highest class of single-seater auto racing sanctioned by the 
Fédération Internationale de l'Automobile (FIA) and owned by the Formula One Group. The FIA Formula One 
World Championship has been one of the premier forms of racing around the world since its inaugaural 
season in 1950.

The dataset contains data from 1950 all the way through the 2019 season, and consists of tables describing 
constructors, race drivers, lap times, pit stops and more.

F1 analysis is created using an iteractive Python notebook, so Jupyter Notebook is required for running 
and modifying the notebook.


## Acknowledgements

The dataset is downloaded from http://ergast.com/mrd/

I am following this [SQL style guide](https://www.sqlstyle.guide)
by Simon Holywell
    

## Instructions to run the notebook
1.  Clone this repository

2.  Download the [database image](http://ergast.com/mrd/db/) and move it into your local repository

3.  Create and activate a virtual environment (optional)

    with [Pip](https://pip.pypa.io/en/stable/):
    
    `python3 -m venv f1_analysis_env`
    
    `source f1_analysis_env/bin/activate`
    
    with [Anaconda](https://www.anaconda.com/distribution/):
    
    `conda create -n f1_analysis_env python=3.7`
    
    `conda activate f1_analysis_env`

4.  Install the required Python libraries 

    with [Pip](https://pip.pypa.io/en/stable/):
    `pip install -r requirements.txt`
    
    with [Anaconda](https://www.anaconda.com/distribution/):
    `conda install -r requirements.txt`
    
5.  Install an ipython kernel for the virtual environment (optional)

    `pip install ipykernel`
    
    `python3 -m ipykernel install --user --name=f1_analysis_env`
    
    You may need to create a new notebook with this environment and copy the content from formula-1-data-analysis.ipynb.
    
6.  Start Jupyter Notebook using the command `jupyter-notebook`

    In the new browser tab, click on formula-1-data-analysis.ipynb, the fast forward button, and "Restart and Run All Cells".


## Jupyter notebook not rendering
Some users have reported that 
[Jupyter notebook is not rendering on GitHub](https://github.com/jupyter/notebook/issues/3035).

If the notebook is not rendering on GitHub, please visit 
[nbviewer](https://nbviewer.jupyter.org/github/jla524/f1-analysis/blob/master/formula-1-data-analysis.ipynb)
to render the notebook.



## Resources 

[Pandas](https://pandas.pydata.org) data analysis library

[Matplotlib](https://matplotlib.org) 2D plotting library

[SQL magic for IPython](https://github.com/catherinedevlin/ipython-sql/blob/master/README.rst) by Catherine Devlin

[Formula 1 Race Data](https://www.kaggle.com/cjgdev/formula-1-race-data-19502017) by Chris G
