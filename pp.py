import numpy as np
import pandas as pd
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
dr=pd.read_csv('rp.csv')
dd=pd.DataFrame(dr)
st.header("DataFrame")
st.write(dd)
rr=dd[["Country name","year","Social support","Freedom to make life choices","Positive affect","Life Ladder"]]
st.write(rr)
st.header("Correlation")
corr=rr.corr()
st.write(corr)
s=sns.heatmap(corr)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.line_chart(data=corr)



