# F1 Analysis
Analyzing Formula 1 race data using Pandas and Matplotlib libraries, and SQL magic for IPython.


## Overview
Formula One (also Formula 1 or F1) is the highest class of single-seater auto racing sanctioned by the 
Fédération Internationale de l'Automobile (FIA) and owned by the Formula One Group. The FIA Formula One 
World Championship has been one of the premier forms of racing around the world since its inaugaural 
season in 1950.

The dataset contains data from 1950 all the way through the 2018 season, and consists of tables describing 
constructors, race drivers, lap times, pit stops and more.

F1 analysis can be run from an iteractive Python notebook. I recommend installing the 
[Anaconda distribution](https://www.anaconda.com/distribution/#download-section)
and using Jupyter Notebook.


## Acknowledgements

The dataset is downloaded from http://ergast.com/mrd/


I am following this [SQL style guide](https://www.sqlstyle.guide)
by Simon Holywell


## Installing Python Libraries

1.  Install with [Pip](https://pip.pypa.io/en/stable/)

    `pip install -U pandas matplotlib ipython-sql`
    
2.  Install with [Anaconda](https://www.anaconda.com/distribution/)

    `conda install -c conda-forge pandas matplotlib ipython-sql`
    

## Instructions to Run
1.  Clone this repository

2.  Download the [dataset](http://ergast.com/mrd/) and move it into the f1-analysis folder

3.  Install the required libraries and execute `python3 clean_data.py`

    Default folder names are input='f1db_csv' and output='clean_f1db'
    
    Users can specify the names like this `python3 clean_data.py input output`
    
4.  Start Jupyter Notebook using the command `jupyter-notebook`


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








