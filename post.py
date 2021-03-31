import requests
my_data={"email":"tinkal6436@gmail.com","password":"tinkal13"}
r=requests.post("https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com%2F",data=my_data)
f=open("myfile.html","w+")
f.write(r.text)
