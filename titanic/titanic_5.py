import seaborn as sns

df = sns.load_dataset('titanic')
df1 = df.drop(['class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone'], axis=1)
df2 = df1.dropna(subset=['age'], how='any', axis=0)
freq_value = df2['embarked'].value_counts(dropna=True).idxmax()
df3 = df2.copy()
df3['embarked'].fillna(freq_value, inplace=True)
df3.loc[df3['sex'] == 'male', 'sex'] = 1
df3.loc[df3['sex'] == 'female', 'sex'] = 0

for idx, item in enumerate(df3['embarked'].unique()):
    df3.loc[df3['embarked'] == item, 'embarked'] = idx

df3 = df3.astype({'sex':'int', 'embarked':'int'})

df3 = (df3 - df3.min()) / (df3.max() - df3.min())
print(df3)

print(df3.groupby(['survived']).mean())