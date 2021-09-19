from airbnb_analysis.consumer import CSV
from airbnb_analysis import consumer
data = CSV.consume('data/AB_NYC_2020.csv')
from airbnb_analysis.analysis import AirbnbAnalyzer
AB2020 = AirbnbAnalyzer(data)



AB2020.room_type_dist_figure('output/AB_NYC_2020_RoomTypePie.png')
AB2020.price_intensity_map('output/AB_NYC_2020_PriceIntensityMap.png')
AB2020.most_reviewed_per_location('output/AB_NYC_2020_MostReviewedPerLocationBar.png')
AB2020.rent_dist_by_neighborhood('output/AB_NYC_2020_RentDistributionByNeighborhoodPie.png')
AB2020.price_bar_per_location('output/AB_NYC_2020_PriceBarPerLocation.png')
AB2020.price_dist_histogram('output/AB_NYC_2020_PriceHistogram.png')
