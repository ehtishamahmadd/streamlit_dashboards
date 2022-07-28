# importing libraries
from matplotlib import animation
import streamlit as st
import plotly.express as px
import pandas as pd

# importing datasets

df = px.data.gapminder()
st.write(df)

# showing list of columns
st.write(df.columns)

# summary statistics
st.write(df.describe())

# managing data according to plotly
#making column of year

year_option = df['year'].unique().tolist()

year = st.selectbox('Which year should we plot?', year_option, 0)
# df= df[df['year'] == year]

# plotting
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='continent',
                 log_x=True, size_max=55, range_x=[100, 100000], range_y=[20, 90],
                 animation_frame='year', animation_group='country') 
fig.update_layout(width =600, title='GDP per Capita vs Life Expectancy')

st.write(fig)