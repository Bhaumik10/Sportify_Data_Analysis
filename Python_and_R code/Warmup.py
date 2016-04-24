# data merge and basic data exploration

import pandas as pd


pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#Pandas Number of rows display
pd.options.display.max_rows = 999

# Load the Data
a = pd.read_csv("~/Desktop/Sportify/user_data_sample.csv")
b = pd.read_csv("~/Desktop/Sportify/end_song_sample.csv")

# Perform the join operation
merged = a.merge(b, on = 'user_id')
#merged.to_csv("~/Desktop/Sportify/output.csv")

#sample data
print merged.head(10)


# Total # of rows & columns for final dataset
total_rows=len(merged.axes[0])
total_cols=len(merged.axes[1])

print total_rows," ", total_cols

# Exploratory Data Analysis

# total No of Paid vs Free subscript
unique_user_id = merged.drop_duplicates('user_id')




####### Above is little bit of Univariate analysis in terms of User base
 ################################################################################################

###############################################################################################################################

#Bivariate analysis   ################################################################################################

################################################################

#By gender vs product
gen_product = unique_user_id.groupby(['gender','product']).user_id.count().reset_index()
print gen_product

#By gender vs age_range
gen_age = unique_user_id.groupby(['gender','age_range']).user_id.count().reset_index()
print gen_age


#By gender total listen
gen_only_user_play_music = merged.groupby(['gender']).ms_played.sum().reset_index()
print gen_only_user_play_music


#By gender vs age_range total listen
gen_age_user_play_music = merged.groupby(['gender','age_range']).ms_played.sum().reset_index()
print gen_age_user_play_music


#By gender vs context total listen
gen_context_user_play_music = merged.groupby(['gender','context']).ms_played.sum().reset_index()
print gen_context_user_play_music



#By gender vs age_range total track
gen_age_user_total_track = merged.groupby(['gender','age_range']).track_id.count().reset_index()
print gen_age_user_total_track

#By gender vs context total track
gen_context_user_total_track = merged.groupby(['gender','context']).track_id.count().reset_index()
print gen_context_user_total_track


#By gender vs context total track
age_context_user_total_track = merged.groupby(['age_range','context']).track_id.count().reset_index()
print age_context_user_total_track



#By only context
only_context_total_track = merged.groupby(['context']).track_id.count().reset_index()
print only_context_total_track
