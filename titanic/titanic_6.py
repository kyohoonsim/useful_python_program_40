import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

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

X = df3[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]
y = df3['survived']

X = preprocessing.StandardScaler().fit(X).transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
acc = metrics.accuracy_score(y_test, y_pred)
print("예측 정확도:", acc)