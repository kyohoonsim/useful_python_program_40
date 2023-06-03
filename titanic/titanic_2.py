import seaborn as sns

df = sns.load_dataset('titanic')
print(df, "\n")
print(df.info())

df1 = df.drop(['class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone'], axis=1)
print(df1, "\n")
print(df1.info())