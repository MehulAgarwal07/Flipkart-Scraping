from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll("div", {"class" : "_3liAhj"})
#print(len(containers))

#print(soup.prettify(containers[0]))

container = containers[0]
#print(container.div.img["alt"])

price = container.findAll("div", {"class":"_1uv9Cb"})
#print(price[0].text)

ratings = container.findAll("div", {"class" : "niH0FQ _36Fcw_"})
#print(ratings[0].text)

filename = "products.csv"
f = open(filename, "w")

headers = "Product_name, Pricing, Ratings\n"
f.write(headers)
for container in containers:
	product_name = container.div.img["alt"]

	price_container = container.findAll("div", {"class":"_1vC4OE"})
	price = price_container[0].text.strip()

	ratings_container = container.findAll("div", {"class" : "hGSR34"})
	rating = ratings_container[0].text

	#print("product_name : " + product_name)
	#print("price : " + price)
	#print("ratings :" + rating)
	price = ''.join(price.split(','))
	print(product_name.replace(",", "|") + "," + price + "," + rating + "\n")
	f.write(product_name.replace(",", "|") + "," + price + "," + rating + "\n")

f.close()