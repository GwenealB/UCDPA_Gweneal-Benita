
import pandas
import matplotlib.pyplot as plot
import seaborn as sns
import numpy as np

class AirbnbAnalyzer:
  DEFAULT_SAVE = None
  def __init__(self, data: pandas.DataFrame, name="Airbnb 0000"):
    self.name = name
    self.data = pandas.DataFrame()
    if(data.empty) :
      print('DATA IS EMPTY!!')
    else :
      self.data = data
  @staticmethod
  def output(save_location):
    if(save_location is None and AirbnbAnalyzer.DEFAULT_SAVE is None):
      plot.show()
    elif (save_location is not None):
      plot.savefig(save_location)
    else:
      plot.savefig(AirbnbAnalyzer.DEFAULT_SAVE)
    plot.close()

  def room_type_dist_figure(self, save_location:str = None):
    room_type = self.data.groupby('room_type')['latitude'].count().reset_index()
    room_type.rename(columns={'latitude':'n_rooms'}, inplace=True)
    plot.figure(figsize=(10,8))
    plot.pie(room_type['n_rooms'],autopct='%1.2f%%', colors=['darkcyan', 'steelblue','powderblue'])
    plot.axis('equal')
    plot.legend(labels=room_type['room_type'],loc='best',fontsize='12')
    plot.title('Room-type Rental Distribution', fontsize='15',color='r')
    self.output(save_location)

  def rent_dist_by_neighborhood(self, save_location:str = None):
    neighbourhood = self.data.groupby('neighbourhood_group')['neighbourhood'].count().reset_index()
    fig,ax = plot.subplots(figsize=(12,8))
    sns.barplot(x=neighbourhood[neighbourhood.columns[0]],
    y=neighbourhood[neighbourhood.columns[1]],color='#004488',ax=ax)
    sns.lineplot(x=neighbourhood[neighbourhood.columns[0]],y=neighbourhood[neighbourhood.columns[1]],color='r',marker='o',ax=ax)
    plot.ylabel('Rentals', fontsize='15')
    plot.xlabel('Borough',fontsize='15')
    plot.title('Rental Distribution by Neighbourhood Group',fontsize='15')
    plot.grid('x')
    self.output(save_location)
    sns.set()

  def price_dist_histogram(self, save_location:str = None):
    # 3 - Histogram plot with price distribution
    price = self.data.loc[:,['neighbourhood','price']].set_index('neighbourhood')
    price_stats = self.data['price'].describe().reset_index()
    price_counts = price.price.value_counts().reset_index()
    price_counts.rename(columns={'index':'price','price':'count'},inplace=True)
    fig2,ax = plot.subplots(figsize=(12,8))
    fig2.patch.set_facecolor('lightgray')
    ax.set_facecolor('lightgray')
    plot.hist(price_counts['price'],bins=30,color='#004488',edgecolor='salmon')
    ax.set_xticks(range(0,10000,500))
    for tick in ax.get_xticklabels():
      tick.set_rotation(45)
    plot.xlabel('Price',fontsize='15')
    plot.ylabel('Rentals', fontsize='15')
    plot.xlim((-0.5,10000))
    plot.title('New York Price-Rental Distribution',fontsize='15')
    self.output(save_location)

  def price_bar_per_location(self, save_location:str = None):
    # 4 - Bar plot with price to location distribution
    loc_price = self.data.groupby(['neighbourhood_group','room_type'])['price'].mean().reset_index()
    locations = loc_price.neighbourhood_group.unique()
    x_rooms1 = [0.8, 3.8, 6.8, 9.8, 12.8]
    x_rooms2 = [1.6, 4.6, 7.6, 10.6, 13.6]
    x_rooms3 = [2.4, 5.4, 8.4, 11.4, 14.4]
    y_values1 = loc_price[loc_price['room_type'] == 'Entire home/apt']['price'].values
    y_values2 = loc_price[loc_price['room_type'] == 'Private room']['price'].values
    y_values3 = loc_price[loc_price['room_type'] == 'Shared room']['price'].values
    fig3,ax2 = plot.subplots(figsize=(16,11))
    fig3.patch.set_facecolor('lightgray')
    ax2.set_facecolor('lightgray')
    plot.bar(x_rooms1, y_values1, color='purple', edgecolor='b')
    plot.bar(x_rooms2, y_values2, color='b', edgecolor='b')
    plot.bar(x_rooms3, y_values3, color='yellowgreen', edgecolor='b')
    ax2.set_xticks(range(1,16,3))
    ax2.set_xticklabels(locations, fontsize='12')
    for tick in ax2.get_xticklabels():
      tick.set_rotation(45)
    plot.xlabel('Location/Room-type',fontsize='15')
    plot.ylabel('Prices', fontsize='15')
    plot.legend(labels=loc_price.room_type.unique(), loc='best')
    plot.title('New York Price-Rental Distribution by Location and Room-type',fontsize='15')
    self.output(save_location)

  def most_reviewed_per_location(self, save_location:str = None):
    # 5 - Most reviewed spots
    review = self.data.sort_values('number_of_reviews',ascending=False)
    top_reviewed = review.loc[:,['neighbourhood','number_of_reviews']][:20]
    top_reviewed = top_reviewed.groupby('neighbourhood').mean().sort_values('number_of_reviews',ascending=False).reset_index()
    fig4,ax3 = plot.subplots(figsize=(12,8))
    sns.barplot(x=top_reviewed['neighbourhood'],y=top_reviewed['number_of_reviews'].values,color='yellowgreen',ax=ax3)
    plot.plot(top_reviewed['number_of_reviews'], marker='o', color='red',linestyle='--')
    plot.ylabel('Reviews', fontsize='15')
    plot.xlabel('Location',fontsize='15')
    plot.ylim((400,580))
    for ax in ax3.get_xticklabels():
      ax.set_rotation(50)
    plot.title('Most-Reviewed Rentals by location',fontsize='15')
    self.output(save_location)
    sns.set()

  def temp(self):
    upper_east = self.data[self.data['neighbourhood'] == 'Upper East Side']
    ninetieth_percentile = np.quantile(upper_east['number_of_reviews'], 0.85)
    upper_east = upper_east[upper_east['number_of_reviews'] >= ninetieth_percentile]
    upper_east = upper_east.sort_values('price',ascending=True)
    private_room = upper_east[upper_east['room_type'] == 'Private room'].reset_index()
    entire_home = upper_east[upper_east['room_type'] == 'Entire home/apt'].reset_index()
    shared_room = upper_east[upper_east['room_type'] == 'Shared room'].reset_index()
    private_cheapest = private_room.loc[0,:].reset_index()
    private_cheapest.rename(columns={'index':'data','0':'values'},inplace=True)
    entire_cheapest = entire_home.loc[0,:].reset_index()
    entire_cheapest.rename(columns={'index':'data','0':'values'},inplace=True)