#import
import pandas as pd 
import statistics
import csv

#reading and making lists of data
df = pd.read_csv("StudentsPerfomance.csv")
maths_score_list = df["math score"]
reading_score_list = df["reading score"]
writing_score_list = df["writing score"]

#finding the mean, median and mode of math scores
maths_score_mean = statistics.mean(maths_score_list)
maths_score_median = statistics.median(maths_score_list)
maths_score_mode = statistics.mode(maths_score_list)

#finding the mean, median and mode of reading scores
reading_score_mean = statistics.mean(reading_score_list)
reading_score_median = statistics.median(reading_score_list)
reading_score_mode = statistics.mode(reading_score_list)

#finding the mean, median and mode of writing scores
writing_score_mean = statistics.mean(writing_score_list)
writing_score_median = statistics.median(writing_score_list)
writing_score_mode = statistics.mode(writing_score_list)

#printing mean, mode and median of math, readong and writing scores
print("Mean,median and mode of math scores are {},{} and {}.".format(maths_score_mean,maths_score_median,maths_score_mode))
print("Mean,median and mode of reading scores are {},{} and {}.".format(reading_score_mean,reading_score_median,reading_score_mode))
print("Mean,median and mode of writing scores are {},{} and {}.".format(writing_score_mean,writing_score_median,writing_score_mode))

#calculating standard deviation
maths_score_std_deviation = statistics.stdev(maths_score_list)
reading_score_std_deviation = statistics.stdev(reading_score_list)
writing_score_std_deviation = statistics.stdev(writing_score_list)

#calculating 1nd , 2nd and 3rd standard deviations for math scores
math_one_stdev_start, math_one_stdev_end = maths_score_mean - maths_score_std_deviation, maths_score_mean + maths_score_std_deviation
math_second_stdev_start, math_second_stdev_end = maths_score_mean - (2*maths_score_std_deviation), maths_score_mean + (2*maths_score_std_deviation)
math_third_stdev_start, math_third_stdev_end = maths_score_mean - (3*maths_score_std_deviation), maths_score_mean + (3*maths_score_std_deviation)

#calculating 1nd , 2nd and 3rd standard deviations for reading scores
reading_one_stdev_start, reading_one_stdev_end = reading_score_mean - reading_score_std_deviation, reading_score_mean + reading_score_std_deviation
reading_second_stdev_start, reading_second_stdev_end = reading_score_mean - (2*reading_score_std_deviation), reading_score_mean + (2*reading_score_std_deviation)
reading_third_stdev_start, reading_third_stdev_end = reading_score_mean - (3*reading_score_std_deviation), reading_score_mean + (3*reading_score_std_deviation)

#calculating 1nd , 2nd and 3rd standard deviations for writing scores
writing_one_stdev_start, writing_one_stdev_end = writing_score_mean - writing_score_std_deviation, writing_score_mean + writing_score_std_deviation
writing_second_stdev_start, writing_second_stdev_end = writing_score_mean - (2*writing_score_std_deviation), writing_score_mean + (2*writing_score_std_deviation)
writing_third_stdev_start, writing_third_stdev_end = writing_score_mean - (3*writing_score_std_deviation), writing_score_mean + (3*writing_score_std_deviation)

#finding the ranges for math scores
m_lod_in_onestdev = [result for result in maths_score_list if result > math_one_stdev_start and result < math_one_stdev_end]
m_lod_in_secondstdev = [result for result in maths_score_list if result > math_second_stdev_start and result < math_second_stdev_end]
m_lod_in_thirdstdev = [result for result in maths_score_list if result > math_third_stdev_start and result < math_third_stdev_end]

#finding the ranges for reading scores
r_lod_in_onestdev = [result for result in reading_score_list if result > reading_one_stdev_start and result < reading_one_stdev_end]
r_lod_in_secondstdev = [result for result in reading_score_list if result > reading_second_stdev_start and result < reading_second_stdev_end]
r_lod_in_thirdstdev = [result for result in reading_score_list if result > reading_third_stdev_start and result < reading_third_stdev_end]

#finding the ranges for writing scores
w_lod_in_onestdev = [result for result in writing_score_list if result > writing_one_stdev_start and result < writing_one_stdev_end]
w_lod_in_secondstdev = [result for result in writing_score_list if result > writing_second_stdev_start and result < writing_second_stdev_end]
w_lod_in_thirdstdev = [result for result in writing_score_list if result > writing_third_stdev_start and result < writing_third_stdev_end]

#printing data percentages for math scores
print("{}% of math scores lying within 1 standard deviation.".format(len(m_lod_in_onestdev*100.0/len(maths_score_list))))
print("{}% of math scores lying within 2 standard deviations.".format(len(m_lod_in_secondstdev*100.0/len(maths_score_list))))
print("{}% of math scores lying within 3 standard deviations.".format(len(m_lod_in_thirdstdev*100.0/len(maths_score_list))))

#printing data percentages for reading scores
print("{}% of reading scores lying within 1 standard deviation.".format(len(r_lod_in_onestdev*100.0/len(reading_score_list))))
print("{}% of reading scores lying within 2 standard deviations.".format(len(r_lod_in_secondstdev*100.0/len(reading_score_list))))
print("{}% of redaing scores lying within 3 standard deviations.".format(len(r_lod_in_thirdstdev*100.0/len(reading_score_list))))

#printing data percentages for writing scores
print("{}% of writing scores lying within 1 standard deviation.".format(len(w_lod_in_onestdev*100.0/len(writing_score_list))))
print("{}% of writing scores lying within 2 standard deviations.".format(len(w_lod_in_secondstdev*100.0/len(writing_score_list))))
print("{}% of writing scores lying within 3 standard deviations.".format(len(w_lod_in_thirdstdev*100.0/len(writing_score_list))))