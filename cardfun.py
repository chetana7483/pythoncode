class card:
  def __init__(self,imageURL,price,rating,description,deliverywithin,comments,brandname):
      self.imageURL=imageURL
      self.price=price
      self.rating=rating
      self.description=description
      self.deliverywithin=deliverywithin
      self.comments=comments
      self.brandname=brandname

  def printalldetails(self):
     print("product imageURL is",self.imageURL)
     print("product price is",self.price)
     print("product rating is",self.rating)
     print("product description is",self.description)
     print("product deliverywithin",self.deliverywithin)
     print("product comments are",self.comments)
     print("product brand name is",self.brandname)

commentforlaptop=["best","this is good","good","not bad"]
laptop=card("http::///",40000,4.5,"12th gen i5core","23rd",commentforlaptop,"hp")
laptop.printalldetails()

commentformobilephone=["best","this is good","good","not bad"]
mobilephone=card("http::///mobile",45000,3.9,"128gb 6gb ram","1stjune",commentformobilephone,"samsang")
mobilephone.printalldetails()

commentforsmartwatch=["best","this is good","good","not bad"]
smartwatch=card("http:://gdsgduys",1200,4.0,"batter good","24thapril",commentforsmartwatch,"fireBoalt")
smartwatch.printalldetails()

