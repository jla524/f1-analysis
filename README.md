# F1 Analysis
Analyzing Formula 1 race data using Pandas and Matplotlib libraries, and SQL
magic for IPython.


## Overview
Formula One (also Formula 1 or F1) is the highest class of single-seater auto
racing sanctioned by the Fédération Internationale de l'Automobile (FIA) and
owned by the Formula One Group. The FIA Formula One World Championship has been
one of the premier forms of racing around the world since its inaugaural season
in 1950.

The dataset contains data from 1950 all the way through the 2019 season, and
consists of tables describing constructors, race drivers, lap times, pit stops
and more.

F1 analysis is created using an iteractive Python notebook, so Jupyter Notebook
is required for running and modifying the notebook.


## Acknowledgements

The dataset is downloaded from http://ergast.com/mrd/

I am following this [SQL style guide][1] by Simon Holywell
 


## Instructions to run the notebook
1.  Clone this repository

    `git clone git@github.com:jla524/f1-analysis.git`
    
    `cd f1-analysis`

2.  Install the required dependencies

    `poetry install`

3.  Download and make the dataset

    `make data`

4.  Use [poetry][3] to create a sub-shell within the virtual environment

    `poetry shell`
    
5.  Start Jupyter Notebook to open the project in a browser

    `jupyter-notebook`

6.  In the new browser tab, select `notebooks` and `formula-1-data-analysis.ipynb`

7.  Click on the fast forward button, and then "Restart and Run All Cells"


## Resources 

[Formula 1 Race Data][4] by Chris G

[Pandas][5] data analysis library

[SQL magic for IPython][6] by Catherine Devlin

[Matplotlib][7] 2D plotting library



[1]: https://www.sqlstyle.guide
[2]: http://ergast.com/mrd/db/
[3]: https://python-poetry.org/docs/#installation
[4]: https://www.kaggle.com/cjgdev/formula-1-race-data-19502017
[5]: https://pandas.pydata.org
[6]: https://github.com/catherinedevlin/ipython-sql/blob/master/README.rst
[7]: https://matplotlib.org
