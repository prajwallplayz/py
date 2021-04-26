import pandas as pd
import plotly.express as px
#data = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
#df=pd.DataFrame(data)
#print(df)

# df=pd.read_csv('linechart.csv')
# fig=px.line(df,x='Year',y='Per capita income',color='Country',title='per capita income')
# fig.show()

# df=pd.read_csv('data.csv')
# fig = px.bar(df, x='Population', y='InternetUsers',color='Country' ,title='usage of internet')
# fig.show()

df = pd.read_csv('data.csv')
fig = px.scatter(df, x='Population', y='Per capita',color='Country' ,title='usage of internet',size_max=60,size='Percentage')
fig.show()
