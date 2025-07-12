import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    return df, iris.target_names


df, target_names = load_data()
# xsst.write(target_names)

st.title("Random Forest Classifier with Iris Dataset")
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df["target"])
st.title("Speacies Prediction Slider")
sepal_length = st.slider(
    "Select Sepal Length",
    min_value=float(df["sepal length (cm)"].min()),
    max_value=float(df["sepal length (cm)"].max()),
    value=float(df["sepal length (cm)"].mean()),
)
petal_length = st.slider(
    "Select Petal Length",
    min_value=float(df["petal length (cm)"].min()),
    max_value=float(df["petal length (cm)"].max()),
    value=float(df["petal length (cm)"].mean()),
)
sepal_width = st.slider(
    "Select Sepal Width",
    min_value=float(df["sepal width (cm)"].min()),
    max_value=float(df["sepal width (cm)"].max()),
    value=float(df["sepal width (cm)"].mean()),
)
petal_width = st.slider(
    "Select Petal Width",
    min_value=float(df["petal width (cm)"].min()),
    max_value=float(df["petal width (cm)"].max()),
    value=float(df["petal width (cm)"].mean()),
)

input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)
st.write("Predicted Species:", target_names[prediction[0]])
st.write("Here is the Iris dataset:")
st.dataframe(df)
