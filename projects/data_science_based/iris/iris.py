import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target

model = RandomForestClassifier()
model.fit(X, y)

sepal_length = st.slider('Sepal Length', min_value=float(X[:, 0].min()), max_value=float(X[:, 0].max()))
sepal_width = st.slider('Sepal Width', min_value=float(X[:, 1].min()), max_value=float(X[:, 1].max()))
petal_length = st.slider('Petal Length', min_value=float(X[:, 2].min()), max_value=float(X[:, 2].max()))
petal_width = st.slider('Petal Width', min_value=float(X[:, 3].min()), max_value=float(X[:, 3].max()))

prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
st.write(f'Predicted class: {iris.target_names[prediction][0]}')