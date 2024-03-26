
# # House Prices Prediction 

# ## Import the library

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt


# ## Load the dataset


train_df = pd.read_csv('./data/train.csv')
test_df= pd.read_csv('./data/test.csv')
train_df.head()


train_df= train_df.drop('Id',axis=1)


print(train_df.shape)


train_df.info()


train_df.describe()


# These statistics assist in identifying outliers, assessing the spread of data, and guiding decisions on normalization or scaling.


columns = train_df.columns
columns


# ## Data Preprocessing
# 


# Let's visualize eatch numerical feature with our target (SalePrice)


df = train_df


# we intreset just about : square footage and number of bedrooms and bathrooms.
# so we will not process all the features


# grap the interesting features
interested_features = ['SalePrice','1stFlrSF','2ndFlrSF','BsmtFinSF1','BsmtFinSF2','GrLivArea','GarageArea', 'TotalBsmtSF', 'FullBath', 'HalfBath','BsmtHalfBath','BsmtFullBath','BedroomAbvGr']


train_df = train_df[interested_features]
test_df = test_df[interested_features[1:]]


train_df.head()


num_columns = train_df.dtypes[train_df.dtypes != 'object']
categorical_columns = train_df.dtypes[train_df.dtypes == 'object']

print("num_columns : ", num_columns.count())
print("categorical_columns : ", categorical_columns.count())


# tracer la matrice de correclation
correlation_matrix = train_df.corr()
plt.figure(figsize=(20,12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")


# visualize the distribution of each feature

fig, ax = plt.subplots(4,3, figsize=(20,20))
for i, ax in enumerate(ax.flat):
    if i < len(interested_features):
        sns.histplot(train_df[interested_features[i]], ax=ax)
        ax.set_title(interested_features[i])


# train_df.query('1stFlrSF > 3000')


# loop over num_columns and plot the scatter plot
for col in num_columns.index:
    plt.figure()
    plt.title(col)
    sns.scatterplot(x=col, y='SalePrice', data=train_df)


sns.histplot(
    train_df,
    x=train_df['SalePrice']
)


train_df['SalePrice'] = np.log1p(train_df['SalePrice'])


sns.histplot(
    train_df,
    x=train_df['SalePrice']
)


# Feature Engineering
train_df['totalsf'] = train_df['1stFlrSF'] + train_df['2ndFlrSF'] + train_df['BsmtFinSF1'] + train_df['BsmtFinSF2']
test_df['totalsf'] = test_df['1stFlrSF'] + test_df['2ndFlrSF'] + test_df['BsmtFinSF1'] + test_df['BsmtFinSF2']

train_df['totalarea'] = train_df['GrLivArea'] + train_df['TotalBsmtSF']
test_df['totalarea'] = test_df['GrLivArea'] + test_df['TotalBsmtSF']

train_df['totalbaths'] = train_df['BsmtFullBath'] + train_df['FullBath'] +  (train_df['BsmtHalfBath'] + train_df['HalfBath']) 
test_df['totalbaths'] = test_df['BsmtFullBath'] + test_df['FullBath'] +  (test_df['BsmtHalfBath'] + test_df['HalfBath']) 


train_df = train_df.drop(columns=['1stFlrSF','2ndFlrSF','BsmtFinSF1','BsmtFinSF2','GrLivArea','TotalBsmtSF', 'FullBath', 'HalfBath','BsmtHalfBath','BsmtFullBath'])
test_df = test_df.drop(columns=['1stFlrSF','2ndFlrSF','BsmtFinSF1','BsmtFinSF2','GrLivArea','TotalBsmtSF', 'FullBath', 'HalfBath','BsmtHalfBath','BsmtFullBath'])



train_df.head()


train_df.info()


# it's look there is some rows that could affect the result
# Let's 


# split the data
X = train_df.drop(columns=['SalePrice'])
y = train_df['SalePrice']


from sklearn.model_selection import train_test_split

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


from sklearn.linear_model import LinearRegression

model = LinearRegression()



# Train the model on the training data
model.fit(X_train, y_train)



# Make predictions on the test data
predictions = model.predict(X_test)



from sklearn.metrics import mean_squared_error

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

import pickle

pickle.dump(model, open('model.pkl', 'wb'))




