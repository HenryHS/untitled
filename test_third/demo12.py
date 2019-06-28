import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures as pf

def scatter_gen(X, label):
    plt.scatter(X, y)
    plt.xlabel(label)
    plt.ylabel("price")
    plt.show()


lb = load_boston()

X = lb.data
y = lb.target

df = pd.DataFrame(X,columns=lb.feature_names)

# for l in lb.feature_names:
#     scatter_gen(df[l],l)

#X = df.drop(['RM','CRIM'],axis=1)

print(X.shape)

X = pf(degree=2,include_bias=False).fit_transform(X)

print(X.shape)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=1)

lr = LinearRegression()

lr.fit(X_train,y_train)

print(lr.coef_,lr.intercept_)

y_predict = lr.predict(X_test)

print(mean_squared_error(y_test,y_predict))
#
print(lr.score(X_test,y_test))

