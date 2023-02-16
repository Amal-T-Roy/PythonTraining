import pandas as pd

# #To read an excel file,pip install openpyxl
# ExcelContent = pd.read_excel('/home/amalr/Desktop/PythonPlan.xlsx')
# print(ExcelContent)

# Read contents of a csv file and store it into a variable called dataframe
EntireContent = pd.read_csv('/home/amalr/Desktop/PythonTraining/Pandas/Test.csv')

print(EntireContent)
print()
print(EntireContent.head(2)) # prints top-n lines
print()
print(EntireContent.tail(4)) # prints bottom-n lines

print('\nExtracting python learners:-\n')
NewFrame = EntireContent[(EntireContent['Course']=='Python')]
print(type(NewFrame))
print(NewFrame)

NumofPythonLearners = len(NewFrame)
print(f"NumOfPyLearners = {NumofPythonLearners}")

print()
CPP = EntireContent[(EntireContent['Course']=="CPP")]
print(CPP)
NumofCPPLearners = len(CPP)
print(f"NumOfC++Learners = {NumofCPPLearners}")