import pandas as pd
import numpy as np


pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Load the Data
a = pd.read_csv("~/Desktop/Sportify/output_session.csv")
len_a = len(a)



# average length ms_played by Session
group_session = a.groupby(['session'])['ms_played'].mean()
print group_session

# No of users by Session
group_session_No_users = a.groupby(['session'])['user_id'].nunique()
print group_session_No_users

# average length ms_played by user_id
group_user_id = a.groupby(['user_id'])['ms_played'].mean()
print group_user_id


# average length ms_played by Session & User_id combine
group_session_user_id = a.groupby(['user_id','session'])['ms_played'].mean()
print group_session_user_id


# average length ms_played by Session & gender combine
group_session_gender = a.groupby(['session','gender_T'])['ms_played'].mean()
print group_session_gender

# average length ms_played by Session & context
group_session_context = a.groupby(['session','context'])['ms_played'].mean()
print group_session_context

# Group by data by session & Country only
group_by_session = a.groupby(['session','US','Non_US'])['ms_played'].mean()
print group_by_session

# Group by data by session & age range
group_by_session_ageRange = a.groupby(['session','age_range'])['ms_played'].mean()
print group_by_session_ageRange

# Group by data by session & product
group_by_session_product = a.groupby(['session','product'])['ms_played'].mean()
print group_by_session_product

print "#############################Correlation Section############################"

# To perform a correlation with all variables to each other
corr = a.corr()
print corr

corr.to_csv("/Users/Bhaumik/Desktop/Sportify/correlation.csv",sep=',',float = 'float64')

print "########### age_of_accts ############"

print "correlation between acct_age_weeks  & ms_played"
print a['acct_age_weeks'].corr(a['ms_played'])

print "########### Gender ############"

print "correlation between gender  & ms_played"
print a['gender_T'].corr(a['ms_played'])


print "########### Demographic ############"

print "correlation between Country_US  & ms_played"
print a['US'].corr(a['ms_played'])

print "correlation between country_Non_US  & ms_played"
print a['Non_US'].corr(a['ms_played'])

print "########### session ############"

print "correlation between session  & ms_played"
print a['session'].corr(a['ms_played'])


print "########### age_group ############"

print "correlation between age_0_17  & ms_played"
print a['age_range_0_17'].corr(a['ms_played'])

print "correlation between age_18_24  & ms_played"
print a['age_range_18_24'].corr(a['ms_played'])

print "correlation between age_range_25_29  & ms_played"
print a['age_range_25_29'].corr(a['ms_played'])

print "correlation between age_range_30_34  & ms_played"
print a['age_range_30_34'].corr(a['ms_played'])

print "correlation between age_range_35_44  & ms_played"
print a['age_range_35_44'].corr(a['ms_played'])

print "correlation between age_range_45_54  & ms_played"
print a['age_range_45_54'].corr(a['ms_played'])

print "correlation between age_range_55+  & ms_played"
print a['age_range_55+'].corr(a['ms_played'])


print "########### context ############"

print "correlation between album  & ms_played"
print a['album'].corr(a['ms_played'])

print "correlation between app  & ms_played"
print a['app'].corr(a['ms_played'])


print "correlation between artist  & ms_played"
print a['artist'].corr(a['ms_played'])


print "correlation between playlist  & ms_played"
print a['playlist'].corr(a['ms_played'])


print "correlation between search  & ms_played"
print a['search'].corr(a['ms_played'])


print "correlation between me  & ms_played"
print a['me'].corr(a['ms_played'])

print "correlation between unknown  & ms_played"
print a['unknown'].corr(a['ms_played'])

print "########### product ############"

print "correlation between premium  & ms_played"
print a['premium'].corr(a['ms_played'])


print "correlation between free  & ms_played"
print a['free'].corr(a['ms_played'])


print "correlation between basic-desktop  & ms_played"
print a['basic-desktop'].corr(a['ms_played'])


print "correlation between open  & ms_played"
print a['open'].corr(a['ms_played'])




