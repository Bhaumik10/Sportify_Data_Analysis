# end_timestamps to datetime conversion and write back into the file

import pandas as pd
import datetime
import numpy as np


#Pandas Number of rows display
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Load the Data
a = pd.read_csv("~/Desktop/Sportify/user_data_sample.csv")
b = pd.read_csv("~/Desktop/Sportify/end_song_sample.csv")

# Perform the join operation
merged = a.merge(b, on = 'user_id')
#merged.to_csv("~/Desktop/Sportify/output.csv")

#sample data
#print merged.head(10)


# Total # of rows & columns for final dataset
total_rows=len(merged.axes[0])
total_cols=len(merged.axes[1])

print total_rows,total_cols


# Determine Unique Track_id
unique_track_id = merged.drop_duplicates('track_id').track_id.count()
#print unique_track_id

# this is in float format
end_time_stamp = merged['end_timestamp'].head(20)
#print end_time_stamp

#This is in int format
int_format = end_time_stamp.astype(np.int64)
#print int_format
#print len(int_format)


# convert Epoch format to Normal Date time
def epoch_datetime_convert(x):
    return datetime.datetime.fromtimestamp(x)


# looping to all rows and writing epoch to date_time conversion row by row
for i in range(len(int_format)):
    merged['date_time'] = pd.to_datetime(merged['end_timestamp'].apply(lambda end_timestamp:epoch_datetime_convert(end_timestamp)))


# Create output file with combine two files and conversion of epoch to date_time format
merged.to_csv("/Users/Bhaumik/Desktop/Sportify/output.csv",sep=',',float = 'float64')

#By gender vs age_range total listen
gen_age_user_play_music = merged.groupby(['user_id','end_timestamp']).ms_played.sum().reset_index()
#print gen_age_user_play_music