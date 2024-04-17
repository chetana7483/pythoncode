class card:
  def __init__(self,imageURL,price,rating,description,deliverywithin,comments,brandname):
      self.imageURL=imageURL
      self.price=price
      self.rating=rating
      self.description=description
      self.deliverywithin=deliverywithin
      self.comments=comments
      self.brandname=brandname

commentforlaptop=["best","this is good","good","not bad"]
laptop=card("http::///",40000,4.5,"12th gen i5core","23rd",commentforlaptop,"hp")
print(laptop.imageURL)
print(laptop.price)
print(laptop.rating)
print(laptop.description)
print(laptop.deliverywithin)
print(laptop.comments)
print(laptop.brandname) 

commentformobilephone=["best","this is good","good","not bad"]
mobilephone=card("http::///mobile",45000,3.9,"128gb 6gb ram","1stjune",commentformobilephone,"samsang")
print(mobilephone.imageURL)
print(mobilephone.price)
print(mobilephone.rating)
print(mobilephone.description)
print(mobilephone.deliverywithin)
print(mobilephone.comments)
print(mobilephone.brandname) 

commentforsmartwatch=["best","this is good","good","not bad"]
smartwatch=card("http:://gdsgduys",1200,4.0,"batter good","24thapril",commentforsmartwatch,"fireBoalt")
print(smartwatch.imageURL)
print(smartwatch.price)
print(smartwatch.rating)
print(smartwatch.description)
print(smartwatch.deliverywithin)
print(smartwatch.comments)
print(smartwatch.brandname) 

