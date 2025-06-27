import pandas as pd

cases_df = pd.read_csv(r"D:\Python\Project\covid_19_india.csv")
vaccine_df = pd.read_csv(r"D:\Python\Project\covid_vaccine_statewise.csv")
test_df = pd.read_csv(r"D:\Python\Project\StatewiseTestingDetails.csv")

print(cases_df.head())
print(vaccine_df.head())
print(test_df.head())

print(cases_df.columns)
print(vaccine_df.columns)
print(test_df.columns)

print(cases_df.info())
print(vaccine_df.info())
print(test_df.info())


# After finding all info of these table , now we get an idea where is the problem in the datasets

# Date in cases_df is in String DataType need to be in DateTime
cases_df['Date'] = pd.to_datetime(cases_df['Date'])
# print(cases_df.info())


# Replace string 'NaN' with real NaN and convert to numeric
# Har value ko number mein convert karo.(, errors='coerce') means agar error aaye to us value ko NaN kar do.
cases_df['ConfirmedIndianNational'] = pd.to_numeric(cases_df['ConfirmedIndianNational'], errors='coerce')
cases_df['ConfirmedForeignNational'] = pd.to_numeric(cases_df['ConfirmedForeignNational'], errors='coerce')
cases_df.fillna(0, inplace=True)
print(cases_df.info())

vaccine_df.columns = vaccine_df.columns.str.strip()  #Ye har column ke naam ke aage/peechhe ka extra space (whitespace) hata deta hai.
vaccine_df['Updated On'] = pd.to_datetime(vaccine_df['Updated On'])
vaccine_df.fillna(0, inplace=True) #Filling missing values with 0
print(vaccine_df.info())


test_df['Date'] = pd.to_datetime(test_df['Date'])
test_df['Negative'] = pd.to_numeric(test_df['Negative'], errors='coerce')
test_df['Positive'] = test_df['Positive'].replace(',', '', regex=True) #Ye esliyea kr rahe h kyuki Nefative ka DataType object tha to esmai numbers jo hote hain vo 12,45 aise bhi ho skte hain to use unko Remove commas krna chyea (ye sbke sath krne ki need nhi h only for DataType with object that should be integer)
test_df['Positive'].fillna(0, inplace=True)
test_df['Negative'].fillna(0, inplace=True)
# print(test_df.info())

#Checking for duplicate in every data file
print("Cases duplicates:", cases_df.duplicated().sum())
print("Vaccine duplicates:", vaccine_df.duplicated().sum())
print("Test duplicates:", test_df.duplicated().sum())

#Removing duplicate form test_df
test_df.drop_duplicates(inplace=True)

#  Check for impossible values (negative cases, doses, etc.)
print((cases_df['Confirmed'] < 0).sum())
print((vaccine_df['Total Doses Administered'] < 0).sum())
print((test_df['TotalSamples'] < 0).sum())

# Column string cleanup

cases_df['State/UnionTerritory'] = cases_df['State/UnionTerritory'].str.strip()
vaccine_df['State'] = vaccine_df['State'].str.strip()
test_df['State'] = test_df['State'].str.strip()

# Saving clean files and removing the index
cases_df.to_csv("clean_cases_df.csv", index=False)
vaccine_df.to_csv("clean_vaccine_df.csv", index=False)
test_df.to_csv("clean_test_df.csv", index=False)

