#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:52:22 2020

@author: diatt17
"""


import pandas as pd

emp = pd.read_csv("../data/Employment.csv", low_memory=False)
covid= pd.read_csv("../data/output/covid.csv")

#remove nation from df adn MSA 
new_emp = emp.iloc[35:]
update= new_emp.iloc[:6707]

rename_emp = update.rename(columns={'Area\nCode':'countyFIPS', 'St Name':'State', 'St':'stateFIPS'})
rename_emp["countyFIPS"] =rename_emp["countyFIPS"].astype(str).astype(int)

column_drop = rename_emp['countyFIPS', 'State', 'Establishment Count', 'January Employment','February Employment','March Employment']
'''
column_drop= rename_emp.drop(['Own','Cnty','NAICS','State','Area Type','Year','Qtr','Ownership', 'Industry','Status Code',
                              'Total Quarterly Wages','Average Weekly Wage', 
                              'Employment Location Quotient Relative to U.S.',
                              'Total Wage Location Quotient Relative to U.S.'], axis=1)
'''

indexname= column_drop[column_drop['Area Type'] == 'State'].index
column_drop.drop(indexname, inplace=True)

column_drop.to_csv("../data/result2.csv")
#group_by_state= column_drop.groupby(['countyFIPS']).sum()

#print(group_by_state)
#group_by_state.to_csv("../data/result2.csv")
#print(column_drop.dtypes)

#print(rename_emp.dtypes)


#df= pd.merge(covid, column_drop,  on= ["countyFIPS"], how='outer')

#df= covid.set_index('countyFIPS').join(new_emp.set_index('countyFIPS'))
#print(df)
#new_df= df.to_csv("../data/result1.csv")