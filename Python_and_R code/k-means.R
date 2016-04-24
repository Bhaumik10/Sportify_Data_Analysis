library(cluster)
library(fpc)

print("k_means clustering Sportify data")

# Getting the information of the working directory
getwd()

# I am using this to clean workspace
#rm(list = ls())

#Read the data file which has all data fields including session informations & Then list the 10 rows from data object
data = read.csv(file ='~/Desktop/Sportify/output_session.csv',header = TRUE,sep = ',')
head(data,10)

# Perform data subset...It only takes numeric value into consideration & again list the 10 rows from data object
data = as.matrix(data[c("acct_age_weeks","ms_played","session","time_delta","gender_T","age_range_0_17","age_range_18_24","age_range_25_29","age_range_30_34","age_range_35_44","age_range_45_54","age_range_55.","album","app","artist","collection","me","playlist","search","unknown","basic.desktop","free","open","premium","US","Non_US")])
head(data,10)

# removing NA/NaN/Inf from the data field/columns
data = data[complete.cases(data),]

# Perform K-means clustering algorithm
(cl <- kmeans(data, 10, iter.max = 100, nstart = 1,algorithm = c("Hartigan-Wong"), trace=FALSE))

# other supported algorithms which we can use instead of "Hartigan-Wong"
# , "Lloyd", "Forgy","MacQueen"

# plotting the clusters 1 way
plot(data, col = cl$cluster)

# plotting the clusters different way
#plotcluster(data, col = cl$cluster)
#clusplot(data, col = cl$cluster, color=TRUE, shade=TRUE,labels=2, lines=0)

# plotting the points
#points(cl$centers, col = 1:26, pch = 19)
points(cl$centers, pch = 19)
