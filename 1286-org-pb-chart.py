import streamlit as st
import pandas as pd

df = pd.DataFrame(
    np.random.randn(50, 2),
    columns=('col %d' % i for i in range(2)))

st.dataframe(df)
st.line_chart(df)
