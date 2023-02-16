import pandas as pd

# Read contents of a csv file and store it into dataframe
Original = pd.read_csv('Test.csv')
print(Original)

# Extract specidic data only
PythonLearners = Original[(Original['Course']=='Python')]
print(PythonLearners)

# Export data to a new csv file
PythonLearners.to_csv('Output.csv')