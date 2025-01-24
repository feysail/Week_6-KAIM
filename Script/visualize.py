import matplotlib.pyplot as plt
import seaborn as sns
def histogram(data):
    column=data.describe().columns.to_list()
    fig,axes=plt.subplots(2,2,figsize=(10,8))
    axes=axes.flatten()
    for i,col in enumerate(column):
      axes[i-1].hist(data[col])
      axes[i-1].set_title(col)
        
def fraud_category(data):
  return data.groupby('FraudResult')['FraudResult'].count()

def fraud_plot(data):
  return data.groupby('FraudResult')['FraudResult'].count().plot(kind='bar')

def heatmap(data):
  column=data.describe().columns.to_list()
  return sns.heatmap(data[column].corr(),cmap='coolwarm',vmax=1,vmin=-1,annot=True)

def boxplot(data):
    column=data.describe().columns.to_list()
    fig,axes=plt.subplots(2,2,figsize=(10,8))
    axes=axes.flatten()
    for i,col in enumerate(column):
      axes[i-1].boxplot(data[col])
     



    