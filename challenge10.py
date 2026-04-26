import pandas as pd
import numpy as np
import random
import math
import copy
roll_number = int(input("enter your number:"))
modify_ind=roll_number%3
threshold = 5.0
def generate(n):
    students =[]
    for i in range(101,101+n):
        rec={
            "id":i,
            "marks":random.randint(40,95),
            "attendance":random.randint(60,100),
            "scores":[random.randint(10,20),random.randint(15,30)]
        }
        students.append(rec)
    return students
def apply_mutation(d_list):
    for idx , student in enumerate(d_list):
        if(modify_ind == 0 and idx ==0)or(modify_ind!=0 and idx%modify_ind==0):
            student["marks"]=student["marks"]+math.sqrt(student["marks"])
            student["scores"][0]+=5
            student["attendance"]=min(100,student["attendance"]+2)
def calc_mean_manual(d_frame):
    marks_list = d_frame["marks"].tolist()
    return sum(marks_list)/len(marks_list)
def analyze_drift(original_df,modified_df):
    original_mean=calc_mean_manual(original_df)
    mod_mean=modified_df["marks"].mean()
    drift = abs(original_mean-mod_mean)
    std_dev =np.std(modified_df["marks"])
    median_val =np.median(modified_df["marks"])
    return drift,std_dev,median_val
raw_data=generate(random.randint(10,15))
original_df =pd.DataFrame(copy.deepcopy(raw_data))
shallow_data=list(raw_data)
deep_data=copy.deepcopy(raw_data)
apply_mutation(shallow_data)
apply_mutation(deep_data)
shallow_df =pd.DataFrame(shallow_data)
deep_df=pd.DataFrame(deep_data)
deep_df["normalized_marks"]=(
    deep_df["marks"]-deep_df["marks"].min()
)/(deep_df["marks"].max()-deep_df["marks"].min())
drift_shallow, _, _ =analyze_drift(original_df,shallow_df)
drift_deep, std_dev, median_val = analyze_drift(original_df,deep_df)
copy_failure = False
for i in range(len(raw_data)):
    if raw_data[i]["marks"] != original_df.iloc[i]["marks"]:
        copy_failure = True
        break
if copy_failure:
    status = "Copy Failure Detected"
elif drift_deep > threshold:
    status = "Critical Drift"
elif drift_deep > 0:
    status = "Minor Drift"
else:
    status = "Stable Data"

summary_tuple = (deep_df["marks"].mean(), drift_deep, std_dev)

print("\nORIGINAL DATAFRAME")
print(original_df.head())

print("\nSHALLOW COPY DATAFRAME")
print(shallow_df.head())
print("\nDEEP COPY DATAFRAME")
print(deep_df.head())
print(f"Drift (Shallow): {drift_shallow:.2f}")
print(f"Drift (Deep): {drift_deep:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Std Dev: {std_dev:.2f}")
print(f"Status: {status}")

print("\nSummary Tuple:", summary_tuple)