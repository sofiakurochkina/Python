import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from pandas.plotting import register_matplotlib_converters 
register_matplotlib_converters()

# Import data 
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates['date'], index_col='date')

# Clean data 
df = df[(df['value'] >= df ['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Draw line plot 
def draw_line_plot():
    plt.figure(figsize=(16,5))
    fig,ax = plt.subplots()
    ax.plot(df.index, df.value)
    ax.set(title='Daily freeCodeCamp Forum Page Views',
    xlabel='Date', ylabel='Page Views')
    fig.savefig('line_plot.png')
    return fig 

def draw_bar_plot():
    # Prepare data for manthly bar plot 
    df_bar=df.groupby([(df.index.year),(df.index.month)]).mean()

    # Draw bar plot 
    ax=df_bar.unstack().plot (kind='bar')
    fig= ax.get_figure()
    ax.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'])
    ax.set(xlabel='Years', ylabel='Average Page Views')
    
    fig.savefig('bar_plot.png')
    return fig

# Draw box plot 
def draw_box_plot():
    # Prepare dara for box plots
    df_box=df.copy()
    df_box.reset_inxe(inplace=True)
    df_box['years']=[d.year for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,ax=plt.subplots(1,2,figsize=(20,7),dpi=80)
    sns.boxplot(x='year', y='value', data = df_box, ax=ax[0]).set(
        xlabel='Year',
        ylabel='Page Views',
        title='Year-wise Box Plot (Trend)'
    )
    sns.boxplot(x='month', y='value', data = df_box.loc[~df_box.year.isin([2016,2019]),:]).set(
         xlabel='Month',
         ylabel='Page Views',
         title='Month-wise Box Plot (Seasonality)'
     )
    fig.savefig('box_plot.png')
    return fig 