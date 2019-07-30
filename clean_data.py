import os, sys, itertools
import numpy as np
import pandas as pd

tables = ['circuits', 'constructor_results', 'constructor_standings', 'constructors', 'driver_standings', \
		  'drivers', 'lap_times', 'pit_stops', 'qualifying', 'races', 'results', 'seasons', 'status']

circuits_n = ['circuitId', 'circuitRef', 'name', 'location', 'country', 'lat', 'lng', 'alt', 'url']
constr_re_n = ['constructorResultsId', 'raceId', 'constructorId', 'points', 'status']
constr_stand_n = ['constructorStandingsId', 'raceId', 'constructorId', \
				  'points', 'position', 'positionText', 'wins']
constr_n = ['constructorId', 'constructorRef', 'name', 'nationality', 'url']
driver_stand_n = ['driverStandingsId', 'raceId', 'driverId', 'points', 'position', 'positionText', 'wins']
drivers_n = ['driverId', 'driverRef', 'number', 'code', 'forename', 'surname', 'dob', 'nationality', 'url']
lap_times_n = ['raceId', 'driverId', 'lap', 'position', 'time', 'milliseconds']
pit_stops_n = ['raceId', 'driverId', 'stop', 'lap', 'time', 'duration', 'milliseconds']
qualifying_n = ['qualifyId', 'raceId', 'constructorId', 'number', 'position', 'q1', 'q2', 'q3']
races_n = ['raceId', 'year', 'round', 'circuitId', 'name', 'date', 'time', 'url']
results_n = ['resultId', 'raceId', 'driverId', 'constructorId', 'number', 'grid', 'position', \
			 'positionText', 'positionOrder', 'points', 'laps', 'time', 'milliseconds', \
			 'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId']
seasons_n = ['year', 'url']
status_n = ['statusId', 'status']

names_list = [circuits_n, constr_re_n, constr_stand_n, constr_n, driver_stand_n, drivers_n, \
		 lap_times_n, pit_stops_n, qualifying_n, races_n, results_n, seasons_n, status_n]


def main(input='f1db_csv/', output='clean_f1db/'):
	assert len(tables) == len(names_list)

	if not os.path.exists(output):
		os.makedirs(output)

	for (table, names) in zip(tables, names_list):
		filename = table + '.csv'
		df = pd.read_csv(input + filename, header=None, names=names)
		df = df.replace(r'\N', np.NaN)
		df.to_csv(output + filename, index=False)


if __name__ == '__main__':
	num_inputs = len(sys.argv)

	if (num_inputs == 1):
		main()	
	elif (num_inputs == 3):
		input = sys.argv[0]
		output = sys.argv[1]
		main(input, output)
	else:
		print("Expected zero or two inputs.")