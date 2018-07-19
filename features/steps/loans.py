from behave import given, when, then

import pandas as pd

banks = pd.read_csv("./data/banks.csv")
covenants = pd.read_csv("./data/covenants.csv")
facilities = pd.read_csv("./data/facilities.csv")
loans = pd.read_csv("./data/loans.csv")
assignments = pd.read_csv("assignments.csv")
yields = pd.read_csv("yields.csv")


@given(u'I follow the covenants of banned_state and max_default_likelihood')
def step_impl(context):
    # Read csv files into a dataframe and
    # merge data frames on facilities & convenants and loans
    # to determine what facilities to assign loans

    filenames = ['./data/large/banks.csv', './data/large/covenants.csv', './data/large/loans.csv',
                 './data/large/facilities.csv']
    dataframes = []
    for f in filenames:
        dataframes.append(pd.read_csv(f))

        df1 = pd.merge(facilities, covenants, on="bank_id", how="outer")
        df2 = pd.merge(loans, facilities, on="interest_rate", how="outer")


@when(u'I figure the expected yield from each loan')
def step_impl(context):
    #   Iterate through the loans with the expected_yield formula
    #   with rules from facilities & covenants

    default_likelihood = 0.01
    loan_interest_rate = 0.15
    amount = 51157
    facility_interest_rate = 0.07
    expected_yield = (
                                 1 - default_likelihood) * loan_interest_rate * amount - default_likelihood * amount - facility_interest_rate * amount
    print(expected_yield)


@then(u'I should see a loan assignment for each facility')
def step_impl(context):
    assignments.to_csv("assignments.csv")
    # print new data to assignments.csv with
    # | Field       | Type    | Description     |
    # | loan_id     | integer | Loan ID         |
    # | facility_id | integer | Facility ID     |



@then(u'I should see an expected yield of each facility')
def step_impl(context):
    yields.to_csv("yields.csv")
    # print new data to assignments.csv with
    # | Field       | Type    | Description     |
    # | facility_id | integer | Facility ID     |
    # | yield       | integer |                 |
