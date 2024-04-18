
# # K-Means Clustering

import random 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.datasets import make_blobs 
import pandas as pd
import seaborn as sns

cust_df = pd.read_csv("Mall_Customers.csv")
cust_df.head()


cust_df.shape


cust_df.info()

df = cust_df.drop(["CustomerID"], axis=1)


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])

from sklearn.preprocessing import StandardScaler

X = df.values[:,:]    
X = np.nan_to_num(X) 
Clus_dataSet = StandardScaler().fit_transform(X)
Clus_dataSet


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(df[['Annual Income (k$)', 'Spending Score (1-100)']])
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


clusterNum = 5
k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 12,random_state=42)
k_means.fit(X)
labels = k_means.labels_

print(labels)


df["Cluster"] = labels 
df.head()


df.groupby('Cluster').mean() 

sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='viridis')
plt.title('Clusters of customers')
plt.show()

import joblib
joblib.dump(k_means, 'model.pkl')


