from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
search=input("Search for: ")
params={"q":search}
r=requests.get("https://www.bing.com/images/search",params=params)

soup = BeautifulSoup(r.text,"html.parser")
links = soup.findAll("a",{"class":"thumb"})
for item in links:
    print(item)
    img_obj=requests.get(item.attrs["href"])
    print("Getting",item.attrs["href"])
    title=item.attrs["href"].split("/")[-1]
    img=Image.open(BytesIO(img_obj.content))
    img.save("scraped_img"+title,img.format)
