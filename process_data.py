import pandas as pd
import pathlib

    
# Read results
df = pd.read_csv(pathlib.Path('./source/results.csv'), encoding='utf-8')

# Read meta data
races = pd.read_csv(pathlib.Path('./source/races.csv'), encoding='utf-8')
drivers = pd.read_csv(pathlib.Path('./source/drivers.csv'), encoding='utf-8')
constructors = pd.read_csv(pathlib.Path('./source/constructors.csv'), encoding='utf-8')
circuits = pd.read_csv(pathlib.Path('./source/circuits.csv'), encoding='utf-8')
status = pd.read_csv(pathlib.Path('./source/status.csv'), encoding='utf-8')

# Join Data
df = df.join(races, on='raceId', how='left', rsuffix='_races') \
    .join(drivers, on='driverId', how='left', rsuffix='_drivers') \
    .join(constructors, on='constructorId', how='left', rsuffix='_constructors') \
    .join(circuits, on='circuitId', how='left', rsuffix='_circuits') \
    .join(status, on='statusId', how='left', rsuffix='_status')

# Filter Data & Columns


# Rename Columns
columns = {
    "resultId": "resultId",
    "year": "seasonYear",
    "round": "seasonRound",
    
    "raceId": "raceId",
    "name": "raceName",
    
    "date": "grandprixDate",
    "time": "grandprixTime",
    "quali_date": "qualifyingDate",
    "quali_time": "qualifyingTime",
    "sprint_date": "sprintDate",
    "sprint_time": "sprintTime",
    
    "driverId": "driverId",
    "number": "driverNumber",
    "driverRef": "driverReference",
    "number_drivers": "driverPreferedNumber",
    "code": "driverCode",
    "forename": "driverForename",
    "surname": "driverSurname",
    "dob": "driverDayOfBirth", 
      
    "constructorId": "constructorId",
    "constructorRef": "constructorReference",
    "name_constructors": "constructorName",
    "nationality_constructors": "constructorNationality",

    "circuitId": "circuitId",
    "circuitRef": "circuitReference",
    "name_circuits": "circuitName",
    "location": "circuitLocation",
    "country": "circuitCountry",
    "lat": "circuitLatitude",
    "lng": "circuitLongitude",
    "alt": "circuitAltitude",  
    
    "grid": "gridPosition",
    "position": "finishingPosition",
    "points": "championshipPoints",
    "laps": "raceLaps",
    "time": "raceTime",
    "milliseconds": "raceMilliseconds",
    "fastestLap": "raceFastestLapId",
    "rank": "raceFastestLapRank",
    "fastestLapTime": "fastestLapTime",
    "fastestLapSpeed": "fastestLapAvgSpeed",
    
    "statusId": "finishingStatusId",
    "status": "finishingStatusDescription",
}

df.rename(mapper=columns, inplace=True, axis='columns')

sorted_columns = [columns[x] for x in columns.keys()]
df = df.reindex(sorted_columns, axis='columns')

# Export Data
df.to_csv('f1_results.csv', sep='|', index=False)

with open('f1_results_columns.txt', 'wt') as f:
    for column_name in df.columns:
        f.write(f"{column_name} ({df.dtypes[column_name]})\n")
        print(column_name, df.dtypes[column_name])

print(df)
print(df.columns)