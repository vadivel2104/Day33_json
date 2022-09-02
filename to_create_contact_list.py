import pandas as pd
# try:
#     data = pd.read_csv("contact_list.csv")
#     print(data.to_dict(orient="records"))
#     df = pd.DataFrame(data)
#     print(df[["Name","Phone Number"]].to_dict(orient="records"))
# else:
#
import pandas.errors

name = input("Enter Name: ")
phone_number = input("Enter Phone Number: ")

df = pd.DataFrame([[name,phone_number]],columns=["Name","Phone Number"])

try:
    data = pd.read_csv("contact_list.csv")
    df.to_csv("contact_list.csv", mode="a", header=False)
except pandas.errors.EmptyDataError:
    df.to_csv("contact_list.csv")








