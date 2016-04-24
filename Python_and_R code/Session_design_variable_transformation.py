import pandas as pd
import numpy as np



pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Load the Data
a = pd.read_csv("~/Desktop/Sportify/output.csv")
len_a = len(a)

#for All data uncomment this


# I am getting 10% of unique user_id data for design session length
a_unique_id = a['user_id'].sample(1000,random_state=10,replace = False)


#Getting those users data for sample
a = a.loc[a['user_id'].isin(a_unique_id), ['user_id','date_time','age_range','acct_age_weeks','ms_played','context','track_id','product','gender','country']]



a = a.sort_values(['user_id','date_time'],kind='mergesort')


total_rows=len(a.axes[0])
total_cols=len(a.axes[1])


print total_rows,total_cols

def time_delta(x,y,i):
    z = (y - x)
    z = (z)/np.timedelta64(1, 'm')
    return z


len_a = len(a) - 1
print len_a
a = a.reset_index()

#pd.to_datetime(merged['end_timestamp'].apply(lambda end_timestamp:epoch_datetime_convert(end_timestamp)))
for i in xrange(len_a):
    x =  pd.to_datetime(a['date_time'][i])
    y =  pd.to_datetime(a['date_time'][i+1])
    #a.loc[i,'time_delta'] = time_delta(x,y,i)   # we can do function call as well
    a.loc[i,'time_delta'] = (y-x)/np.timedelta64(1,'m')


print "########################################################"

# Gets the mean to determine after what value of time delta we need to create a new sessions
print a[a['time_delta'] >= 0].mean() # To solve the problem of last row NaN




# Define session here
s_int = 1
for i in xrange(len_a):
    #print a.loc[i,'time_delta'].round(3)
    #
    if a.loc[i,'user_id'] == a.loc[i+1,'user_id'] :
        s_int = s_int
    else:
        s_int = 1
    if a.loc[i,'time_delta'].round(3) <= 32.600:
        a.loc[i,'session'] = s_int
    elif a.loc[i,'time_delta'].round(3) > 32.610:
        s_int = s_int + 1
        a.loc[i,'session'] = s_int
    else:
        a.loc[i,'session'] = s_int


# male_female Transformation
for i in xrange(len_a+1):
    if a.loc[i,'gender'] == 'male':
        a.loc[i,'gender_T'] = 1
    elif a.loc[i,'gender'] == 'female':
        a.loc[i,'gender_T'] = 2
    else:
        a.loc[i,'gender_T'] = 0

# accts_age Transformation

a['age_range_0_17'] = 0
a['age_range_18_24'] = 0
a['age_range_25_29'] = 0
a['age_range_30_34'] = 0
a['age_range_35_44'] = 0
a['age_range_45_54'] = 0
a['age_range_55+'] = 0



for i in xrange(len_a+1):
    if a.loc[i,'age_range'] == '0 - 17':
        a.loc[i,'age_range_0_17'] = 1
    elif a.loc[i,'age_range'] == '18 - 24':
        a.loc[i,'age_range_18_24'] = 1
    elif a.loc[i,'age_range'] == '25 - 29':
        a.loc[i,'age_range_25_29'] = 1
    elif a.loc[i,'age_range'] == '30 - 34':
        a.loc[i,'age_range_30_34'] = 1
    elif a.loc[i,'age_range'] == '35 - 44':
        a.loc[i,'age_range_35_44'] = 1
    elif a.loc[i,'age_range'] == '45 - 54':
        a.loc[i,'age_range_45_54'] = 1
    elif a.loc[i,'age_range'] == '55+':
        a.loc[i,'age_range_55+'] = 1

# Context Transformation

a['album'] = 0
a['app'] = 0
a['artist'] = 0
a['collection'] = 0
a['me'] = 0
a['playlist'] = 0
a['search'] = 0
a['unknown'] = 0

print a.dtypes

for i in xrange(len_a + 1):
    if a.loc[i,'context'] == 'album':
        a.loc[i,'album'] = 1
    elif a.loc[i,'context'] == 'app':
        a.loc[i,'app'] = 1
    elif a.loc[i,'context'] == 'artist':
        a.loc[i,'artist'] = 1
    elif a.loc[i,'context'] == 'collection':
        a.loc[i,'collection'] = 1
    elif a.loc[i,'context'] == 'me':
        a.loc[i,'me'] = 1
    elif a.loc[i,'context'] == 'playlist':
        a.loc[i,'playlist'] = 1
    elif a.loc[i,'context'] == 'search':
        a.loc[i,'search'] = 1
    elif a.loc[i,'context'] == 'unknown':
        a.loc[i,'unknown'] = 1


# Product Transformation

a['basic-desktop'] = 0
a['free'] = 0
a['open'] = 0
a['premium'] = 0



for i in xrange(len_a + 1):
    if a.loc[i,'product'] == 'basic-desktop':
        a.loc[i,'basic-desktop'] = 1
    elif a.loc[i,'product'] == 'free':
        a.loc[i,'free'] = 1
    elif a.loc[i,'product'] == 'open':
        a.loc[i,'open'] = 1
    elif a.loc[i,'product'] == 'premium':
        a.loc[i,'premium'] = 1



# country Demographic USA vs Non-USA
a['US'] = 0
a['Non_US'] = 0


for i in xrange(len_a + 1):
    if a.loc[i,'country'] == 'US':
        a.loc[i,'US'] = 1
    elif a.loc[i,'country'] != 'US':
        a.loc[i,'Non_US'] = 1

#write back the data to file for further analytics purpose.
a.to_csv("/Users/Bhaumik/Desktop/Sportify/output_session.csv",sep=',',float = 'float64')