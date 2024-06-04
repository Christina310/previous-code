import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly as plotly
import sklearn as skl

#Create data
data = {
    'price': [1, 2, 3, 4, 5, 6, 6.5, 7, 8, 9, 10],
    'quantity': [100, 90, 80, 70, 60, 50, 45, 40, 30, 20, 10]
}
df = pd.DataFrame(data)
df.to_csv('price & quantity.csv', index=False)

# Import data
df = pd.read_csv('/Users/xiexinyi/Desktop/Wisconsin/2024 Spring/AAE 625/HW1/pythonProject/price & quantity.csv')
df = df.rename(columns={'price':'P'})
df = df.rename(columns={'quantity':'Q'})
plt.figure(figsize=(10, 6))
sns.lineplot(x='P', y='Q', data=df, color='red', label='Demand Curve')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Demand Curve')
plt.legend()
plt.show()

# ------------Point estimation-------------
df = df[['P','Q']]
# pct:
df['P_pct'] = df['P'].pct_change()
df['Q_pct'] = df['Q'].pct_change()
df['Price_Elas'] = df['Q_pct']/df['P_pct']
print(df['Price_Elas'])
df['Rev'] = df['P'] * df['Q']
df['Rev_pct'] = df['Rev'].pct_change()
df['Revenue_Elas'] = df['Rev_pct']/df['P_pct']
print(df['Revenue_Elas'])

#Create two figures
#Demand curve and revenue
x1 = df['P']
y1 = df['Q']
z1=df['Rev']
z2 = df['Price_Elas']
trace1 = go.Scatter(
    x=x1,
    y=y1,
    name='Demand Curve'
)
trace2 = go.Scatter(
    x=x1,
    y=z1,
    name='Revenue',
    yaxis='y2'
)
data1 = [trace1, trace2]
layout1 = go.Layout(
    title='Demand curve and revenue',
    yaxis=dict(
        title='Quantity'
    ),
    yaxis2=dict(
        title='Revenue',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    ),
        xaxis=dict(
        title='Price',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
))
fig = go.Figure(data=data1, layout=layout1)
fig.show()
#Demand curve and own-price elasticity
trace3 = go.Scatter(
    x=x1,
    y=y1,
    name='Demand Curve'
)
trace4 = go.Scatter(
    x=x1,
    y=z2,
    name='Elasticity',
    yaxis='y2'
)
data2 = [trace3, trace4]
layout2 = go.Layout(
    title='Demand curve and own-price elasticity',
    yaxis=dict(
        title='Quantity'
    ),
    yaxis2=dict(
        title='Price Elasticity of Demand',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    ),
        xaxis=dict(
        title='Price',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
))
fig = go.Figure(data=data2, layout=layout2)
fig.show()

##Price elasticity measures how responsive the quantity demanded of a good is to changes in its price. I used marginal revenue with respect to price to calculate revenue elasticity. Thus revenue elasticity measures how responsive revenue is to changes in price.
##Revenue increases with price. As the value of revenue elasticity changes from positive to negative and becomes more negative, it indicates that revenue decreases as the price of goods increases.
##The shift from positive to negative revenue elasticity corresponds to price elasticity becoming more elastic.

##I make some comments for this code file.




