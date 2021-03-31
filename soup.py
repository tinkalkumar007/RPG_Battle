from bs4 import BeautifulSoup
import requests
search=input("Enter search term ")
params={"q":search}
r=requests.get("https://www.bing.com/search",params=params)# here we requests items in search box

soup=BeautifulSoup(r.text,"html.parser")# here we saved all data of web page. In html.parser data is saved in text format. Now once we get soup equal to entire webpage.
results=soup.find("ol",{"id":"b_results"})# we are going through the soup for the first instance of ordered list with an id of b_results. so this is going to be element you are looking for and this list is going to contain any attributes looking for and then from within the results we. can use find all the method and we are going to pass it the elements we are looking for within the results, and then the class attribute you are looking for  
links=soup.findAll("li",{"class":"b_algo"})# so this is going to find all list items with the class b_algo and store them in lists called links

for item in links:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]# if you want speific attribute from an element. you use the attrs and then in the list
    if item_text and item_href:
       print(item_text)
       print(item_href)
# so now we are going to talk about parent parsing find parent of an element as well as children parsing. let's go ahead...
       #print("Parent.",item.find("a").parent)
# now we need to print out summary. Now we are going to need to go back one more ".parent"
       #print("summary",item.find("a").parent.parent.find("p").text)
       '''children=item.children # this is going to compile a list of all children element of that item list and to give you an example
       for child in children:
           print("Child:",child)'''
# we can find sbiling of that 
       children=item.find("h2")
       print("Next sibling of the h2 :", children.next_sibling)


