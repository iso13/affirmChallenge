import pandas as pd

# read csv files to a data frame

assignments_small = pd.read_csv("./data/small/assignments.csv")
banks_small = pd.read_csv("./data/small/banks.csv")
covenants_small = pd.read_csv("./data/small/covenants.csv")
facilities_small = pd.read_csv("./data/small/facilities.csv")
loans_small = pd.read_csv("./data/small/loans.csv")
yields_small = pd.read_csv("./data/small/yields.csv")

banks_large = pd.read_csv("./data/large/banks.csv")
covenants_large = pd.read_csv("./data/large/covenants.csv")
facilities_large = pd.read_csv("./data/large/facilities.csv")
loans_large = pd.read_csv("./data/large/loans.csv")

# figure the expected yield for each facilities
# expected_yield = (1 - default_likelihood) * (loan_interest_rate * amount) - (default_likelihood * amount) - (
#             facility_interest_rate * amount)

# report
