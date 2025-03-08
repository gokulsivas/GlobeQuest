import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

all_tour_details = []

for i in range(1,25,1):
    # URL of the package page
    url = "https://www.veenaworld.com/world/page/"+ str(i)
    print(url)

    # Send request to fetch the content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    # Find all result cards in case there are multiple tours listed
    Search_card_Wpr= soup.find_all('div', class_='searchCardWpr')

    for scw in Search_card_Wpr:
        tours = scw.find_all('div', 'searchCard')
        for tour in tours:
            tour_details = {}
            #print(tour)
            img_tag = tour.find('div', class_='imageWpr')
            img_tg = img_tag.find('img')
            alt_text = img_tg.get('alt') if img_tg else 'NA' 
            image_url = img_tg.get('src') if img_tg else 'NA'
            #print(image_url)

            price_starts_from_tag = tour.find('div', class_='price')
            price_starts_from = price_starts_from_tag.get_text(strip=True) if price_starts_from_tag else 'NA'

            days_tag = tour.find('div', class_='product-shorts') 
            days = days_tag.find('h6').get_text(strip=True) if days_tag else 'NA'

            title_tag =tour.find('h3', class_='cardTitle') 
            title = title_tag.get_text(strip=True) if title_tag else 'NA'

            tour_highlights_tag  = tour.find('div',class_='highlight-text')
            tour_highlights = tour_highlights_tag.find('p').get_text(strip=True) if tour_highlights_tag else 'NA'
            
            tour_type_tag = tour.find('div', class_='tourType')
            tour_type = tour_type_tag.get_text(strip=True) if tour_type_tag else 'NA'

            tour_for_tag = tour.find('div',class_='shortTrip')
            tour_for = tour_for_tag.find('span').get_text(strip=True) if tour_for_tag else 'NA'

            price_note_tag = tour.find('div', class_='priceNote')    
            price_note = price_note_tag.get_text(strip=True) if price_note_tag else 'NA'
            
            """
            print(price_starts_from)
            print(alt_text)
            print(image_url)
            print(days)
            print(title)
            print(tour_highlights)
            print(tour_type)
            print(tour_for)
            print(price_note)
            """
            print('page-',i)
            print(title)
            
            # create dic object
            tour_details['title']=title
            tour_details['days']=days
            tour_details['image_url']=image_url
            tour_details['image_alt_text']=alt_text
            tour_details['tour_type']=tour_type
            tour_details['tour_for']=tour_for
            tour_details['price']=price_starts_from
            tour_details['price_note']=price_note
            tour_details['tour_highlights']=tour_highlights

            # append it global list
            all_tour_details.append(tour_details)
            #print(all_tour_details)

df = pd.DataFrame(all_tour_details)
print(df)
df.to_csv('all_tour_details.csv')