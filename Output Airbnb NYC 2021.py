from airbnb_analysis.consumer import SQLite

data = SQLite.consume(SQLite.AB_NYC_2021)
from airbnb_analysis.analysis import AirbnbAnalyzer
AB2021 = AirbnbAnalyzer(data)



AB2021.room_type_dist_figure('output/AB_NYC_2021_RoomTypePie.png')
AB2021.price_intensity_map('output/AB_NYC_2021_PriceIntensityMap.png')
AB2021.most_reviewed_per_location('output/AB_NYC_2021_MostReviewedPerLocationBar.png')
AB2021.rent_dist_by_neighborhood('output/AB_NYC_2021_RentDistributionByNeighborhoodPie.png')
AB2021.price_bar_per_location('output/AB_NYC_2021_PriceBarPerLocation.png')
AB2021.price_dist_histogram('output/AB_NYC_2021_PriceHistogram.png')
