from airbnb_analysis.consumer import CSV
from airbnb_analysis import consumer
data = CSV.consume('data/AB_NYC_2019.csv')
from airbnb_analysis.analysis import AirbnbAnalyzer
AB2019 = AirbnbAnalyzer(data)



AB2019.room_type_dist_figure('output/AB_NYC_2019_RoomTypePie.png')
AB2019.price_intensity_map('output/AB_NYC_2019_PriceIntensityMap.png')
AB2019.most_reviewed_per_location('output/AB_NYC_2019_MostReviewedPerLocationBar.png')
AB2019.rent_dist_by_neighborhood('output/AB_NYC_2019_RentDistributionByNeighborhoodPie.png')
AB2019.price_bar_per_location('output/AB_NYC_2019_PriceBarPerLocation.png')
AB2019.price_dist_histogram('output/AB_NYC_2019_PriceHistogram.png')
