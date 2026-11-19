import pandas as pd


# Series
# DataFrame


list = [
    ["Abdelhafid" , 20 , "ELjadida"] ,
    ["Chakib" , 19 , " jadida"] ,
    ["Chakib" , 19 , " jadida"] ,
    ["Chakib" , 19 , " jadida"] ,
    ["Chakib" , 19 , " jadida"] ,
    ["Chakib" , 19 , " jadida"] ,
    ["Chakib" , 19 , " jadida"] ,
]
newlist = pd.DataFrame(list)
print(newlist)

df = pd.read_csv("hello.csv")
print(df)

sr = pd.Series([1,True,3,False,[1, "A" , "B"]])
print(sr[4])




