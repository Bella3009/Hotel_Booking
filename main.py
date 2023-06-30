import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id":str})


class Hotel:
    def __init__(self, id):
        self.id = id
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the Hotel is available"""
        availability = df.loc[df["id"] == self.id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class Reservation:
    def __init__(self, client_name, hotel_obj):
        self.client_name = client_name
        self.hotel = hotel_obj

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.client_name}
        Hotel name: {self.hotel.name}        
        """

        return content


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reserve = Reservation(name, hotel)
    print(reserve.generate())
else:
    print("Hotel is not available")
