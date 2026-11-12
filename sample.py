import pandas as pd

df = pd.read_csv(r'C:\Users\Sorin\Downloads\BasicCompanyDataAsOneFile-2026-11-01\BasicCompanyDataAsOneFile-2026-11-01.csv')

df.columns = df.columns.str.strip()

active_companies = df[df['CompanyStatus'] == 'Active']

sample_5 = active_companies.sample(n=5)

print("\n Esantionul de 5 companii active: ")
print(sample_5[['CompanyName', 'CompanyNumber', 'CompanyStatus']])