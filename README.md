# zomato-analysis

We were always fascinated by the food culture of Bengaluru. Restaurants from all over the world can
be found here in Bengaluru. From United States to Japan, Russia to Antarctica, you get all type of
cuisines here. Delivery, Dine-out, Pubs, Bars, Drinks,Buffet, Desserts you name it and Bengaluru has
it. Bengaluru is best place for foodies. The number of restaurant are increasing day by day. Currently
which stands at approximately 12,000 restaurants. With such an high number of restaurants. This
industry hasn't been saturated yet. And new restaurants are opening every day. However it has
become difficult for them to compete with already established restaurants. The key issues that
continue to pose a challenge to them include high real estate costs, rising food costs, shortage of
quality manpower, fragmented supply chain and over-licensing. This Zomato data aims at analysing
demography of the location. Most importantly it will help new restaurants in deciding their theme,
menus, cuisine, cost etc for a particular location. It also aims at finding similarity between
neighborhoods of Bengaluru on the basis of food. The dataset also contains reviews for each of the
restaurant which will help in finding overall rating for the place.

We are trying to come with a Website to integrate the dashboard using python based Django Framework.

The basic idea of analyzing the Zomato dataset is to get a fair idea about the factors
affecting the establishment of different types of restaurant at different places in
Bengaluru, aggregate rating of each restaurant, Bengaluru being one such city has more
than 12,000 restaurants with restaurants serving dishes from all over the world. With
each day new restaurants opening the industry hasn't been saturated yet and the demand
is increasing day by day. In Spite of increasing demand it has become difficult for new
restaurants to compete with established restaurants. Most of them serving the same
food. Bengaluru being an IT capital of India. Most of the people here are dependent
mainly on the restaurant food as they don’t have time to cook for themselves. With such
an overwhelming demand of restaurants it has therefore become important to study the
demography of a location. What kind of a food is more popular in a locality. Do the entire
locality loves vegetarian food. If yes then is that locality populated by a particular sect of
people for eg. Jain, Marwaris, Gujaratis who are mostly vegetarian.
These kind of analysis can be done using the data, by studying the factors such as

• Location of the restaurant

• Approx Price of food

• Theme based restaurant or not

• Which locality of that city serves that cuisines with maximum number of restaurants

• The needs of people who are striving to get the best cuisine of the neighborhood

• Is a particular neighborhood famous for its own kind of food.

“Just so that you have a good meal the next time you step out”
The data is accurate to that available on the zomato website until 15 March 2019. The
data was scraped from Zomato in two phase. After going through the structure of the
website I found that for each neighborhood there are 6-7 category of restaurants viz.
Buffet, Cafes, Delivery, Desserts, Dine-out, Drinks & nightlife, Pubs and bars.

## Dataset description :

The collected data has been stored in the Comma Separated Value file Zomato.csv. Each restaurant
in the dataset is uniquely identified by its Restaurant Id. Every Restaurant contains the following
variables:
• Restaurant Id: Unique id of every restaurant across various cities of the world
• Restaurant Name: Name of the restaurant
• Country Code: Country in which restaurant is located
• City: City in which restaurant is located
• Address: Address of the restaurant
• Locality: Location in the city
• Locality Verbose: Detailed description of the locality
• Longitude: Longitude coordinate of the restaurant's location
• Latitude: Latitude coordinate of the restaurant's location
• Cuisines: Cuisines offered by the restaurant
• Average Cost for two: Cost for two people in different currencies 👫
• Currency: Currency of the country
• Has Table booking: yes/no
• Has Online delivery: yes/ no
• Is delivering: yes/ no
• Switch to order menu: yes/no
• Price range: range of price of food
• Aggregate Rating: Average rating out of 5
• Rating color: depending upon the average rating color
• Rating text: text on the basis of rating of rating
• Votes: Number of ratings casted by people
