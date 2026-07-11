import pandas as pd
import pyreadstat


df5, meta5 = pyreadstat.read_sav('fs-kpk.sav')

df6, meta6 = pyreadstat.read_sav('hh-kpk.sav')


merged_df3 = pd.merge(df5, df6, on=['HH1', 'HH2'], how='inner')
print("Merged DataFrame info:")
merged_df3.info()
print("\nMerged DataFrame head:")
display(merged_df3.head())

merged_df3.to_csv("kpk.csv", index=False)
merged_df3.to_csv("kpk.csv", index=False)


df7, meta7 = pyreadstat.read_sav('fs-balochistan.sav')
print("df loaded successfully using pyreadstat.")
for col in df7.columns:
    print(col)

df8, meta8 = pyreadstat.read_sav('hh-balochistan.sav')
print("df loaded successfully using pyreadstat.")
for col in df8.columns:
    print(col)
merged_df3 = pd.merge(df7, df8, on=['HH1', 'HH2'], how='inner')
merged_df3.to_csv("balochistan.csv", index=False)



df1, meta1 = pyreadstat.read_sav('fs-sindh.sav')
print("df loaded successfully using pyreadstat.")
for col in df1.columns:
    print(col)

df2, meta2 = pyreadstat.read_sav('hh-sindh.sav')
print("df loaded successfully using pyreadstat.")
for col in df2.columns:
    print(col)

merged_df1 = pd.merge(df1, df2, on=['HH1', 'HH2'], how='inner')

merged_df1.to_csv("sindh.csv", index=False)

df3, meta3 = pyreadstat.read_sav('fs-punjab.sav')
print("df loaded successfully using pyreadstat.")
for col in df3.columns:
    print(col)

df4, meta4 = pyreadstat.read_sav('hh-punjab.sav')
print("df loaded successfully using pyreadstat.")
for col in df4.columns:
    print(col)

merged_df2 = pd.merge(df3, df4, on=['HH1', 'HH2'], how='inner')
merged_df2.to_csv("punjab.csv", index=False)

df1=pd.read_csv("sindh.csv")
df2=pd.read_csv("punjab.csv")
df3=pd.read_csv("balochistan.csv")
df4=pd.read_csv("kpk.csv")
province_df = pd.concat([df1, df2,df3,df4], ignore_index=True)

province_df.info()

province_df.to_csv("province.csv", index=False)

df=pd.read_csv("province.csv")

columns_to_keep = [

    'HH1', 'HH2',          # Merge keys (household + child ID) 
    'P_code',              # Province/region code 
               'hh6_x',                 # Urban/rural indicator 
    'FSAGE',               # Age groups of child (categorical)
    'HC13',                # internet access
    'WS1',                 # main water source
    'HH26A',               # Child Rank 
    'HH26B',               # Child Line Number
    'HH26C',               # Child Age 
    'CB7',                 # Currently attending school (DV)
    'CB4',                 # Ever attended school (robustness check)
    'CB9',                 # Attended previous school year (robustness check)
    'PR13',                # Missed class due to teacher absence (overall)
    'melevel',             # Mother’s educational groups (categorical)
    'helevel',             # Household head’s education 
    'windex5_x',             # Wealth index quintile
    'windex10_x',            # Wealth index decile
    'wscore_x'               # wealth score combined
               'hh48',                # Household members
    'HHSEX',               # Sex of household head 
    'HC8',                 # Access to electricity
    'fselevel',            # Child's education
    'PR12C',               # Missed class due to teacher absence oe strike
    'CB3',                 # Age of child 
    'division',            # Divisions
    'HH7',                 # districts
    'CB5A',                # highest lvl of education
    'hhage'                 # hh age
]


df_clean = df[[col for col in columns_to_keep if col in df.columns]]

print(df_clean)
df_clean.to_csv("final-3.csv", index=False)




