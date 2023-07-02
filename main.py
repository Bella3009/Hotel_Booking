import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_card = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")


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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiry, holder, cvc):
        card_data = {"number": self.number, "expiry": expiry,
                     "holder": holder, "cvc": cvc}
        if card_data in df_card:
            return True
        else:
            return False


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.available():
    credit_card = CreditCard("1234")
    if credit_card.validate(expiry="12/26", holder="John Smith", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        reserve = Reservation(name, hotel)
        print(reserve.generate())
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not available")
