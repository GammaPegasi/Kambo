# from webscrap.models import Prod
import requests
from bs4 import BeautifulSoup
import sys

# url1 = "https://listado.mercadolibre.com.uy/ford-escort#D[A:ford-escort,B:0]"
# url2 = "https://listado.mercadolibre.com.uy/mercedes-benz#D[A:mercedes-benz,B:1]"
# url3 = 'https://listado.mercadolibre.com.uy/citroen-c3#D[A:citroen-c3]'
# url4 = 'https://listado.mercadolibre.com.uy/autos-honda#D[A:autos-honda-]'
# url5 = 'https://listado.mercadolibre.com.uy/bmw#D[A:bmw]'
# url6 = 'https://autos.mercadolibre.com.uy/renault/'

# vect = []

# vect.append('https://listado.mercadolibre.com.uy/chebrolettt-corsa#D[A:chebrolettt-corsa,B:0]')
# vect.append('https://autos.mercadolibre.com.uy/chevrolet/corsa/chebrolettt-corsa_Desde_49')
# vect.append('https://autos.mercadolibre.com.uy/chevrolet/corsa/chebrolettt-corsa_Desde_97')
# vect.append('https://autos.mercadolibre.com.uy/chevrolet/corsa/chebrolettt-corsa_Desde_145')
# vect.append('https://autos.mercadolibre.com.uy/chevrolet/corsa/chebrolettt-corsa_Desde_193')
# vect.append('https://autos.mercadolibre.com.uy/chevrolet/corsa/chebrolettt-corsa_Desde_241')

# inicio = 'https://autos.mercadolibre.com.uy/volkswagen/'
# inicio = 'https://listado.mercadolibre.com.uy/hyundai#D[A:hyundai-]'
# inicio = 'https://listado.mercadolibre.com.uy/ford#D[A:ford]'
# inicio = 'https://listado.mercadolibre.com.uy/fiat#D[A:fiat]'
# inicio = 'https://listado.mercadolibre.com.uy/citroen#D[A:citroen,B:5]'

inicio = 'https://autos.mercadolibre.com.uy/nissan/'
inicio = 'https://autos.mercadolibre.com.uy/toyota/'
inicio = 'https://autos.mercadolibre.com.uy/suzuki/'
inicio = 'https://autos.mercadolibre.com.uy/mercedes-benz/'
inicio = 'https://autos.mercadolibre.com.uy/citroen/'


def scrap(site):

	page = requests.get(site)
	soup = BeautifulSoup(page.content, 'html.parser')
	# print(soup.prettify())
	length  = len(soup.find_all(class_='rowItem'))
	lst_row = soup.find_all(class_='rowItem')

	for i in range(0, length):
		currency = lst_row[i].find(class_="price__symbol").text
		price = lst_row[i].find(class_="price__fraction").text
		attrs = lst_row[i].find(class_="item__attrs").text
		title = lst_row[i].find(class_="main-title").text
		location = lst_row[i].find(class_="item__location").get_text()
    	
		img_src = "#"

		try:
			img_src = lst_row[i].find('img')['src']
		except:
			try:
				img_src = lst_row[i].find('img')['data-src']
			except:
				e = sys.exc_info()[0]
				print( "Error: %s" % e )
			
		product_page_url  = lst_row[i].find('a')['href']

# 		p = Prod()
		
# 		p.title = title
# 		p.currency = currency
# 		p.attrs = attrs
# 		p.price = price
# 		p.location = location
# 		p.prod_url = product_page_url
# 		p.image_src = img_src
		
# 		p.save()

		print('{} [{}] [{}] {} {} {}'.format(i, title, attrs, currency, price, location))
		print(img_src)
		print(product_page_url,  '\n')

	next_page = soup.find(class_='pagination__next').find("a")['href']

	if next_page == '#':
	    print('This is the last page\n')
	else: 
	    print('Next page -> ', next_page)
	    scrap(next_page)


# for i in vect:
#  	scrap(i)

scrap(inicio)
