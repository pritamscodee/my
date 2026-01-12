from orm_init import Base
from sqlalchemy import Column,Integer,String, Mapped, mapped_column, relationship

class Customer(Base):
    id=Mapped[int]=mapped_column(Integer,primary_key=True)
    address=Mapped[str]=mapped_column(String)
    city=Mapped[str]=mapped_column(String)
    phone_number=Mapped[int]=mapped_column(Integer)
    reviews=Mapped[str]=mapped_column(String)

    Added_cart:Mapped["Cart"]=relationship(
         back_populates="customer_cart"

    )

    Buied_items:Mapped["Buieditems"]=relationship(
           back_populates="customer_buied"
    )

    
class Cart(Base):
    item_id=Mapped[int]=mapped_column(Integer)
    item_name=Mapped[str]=mapped_column(String)
    item_price=Mapped[int]=mapped_column(Integer)
    item_Instock=Mapped[bool]=mapped_column(bool)

    customer_cart:Mapped["Customer"]=relationship(
        back_populates=" Added_cart"
    ) 
     


class Buieditems(Base):
    item_id=Mapped[int]=mapped_column(Integer)
    item_name=Mapped[str]=mapped_column(String)
    item_price=Mapped[int]=mapped_column(Integer)

    customer_buied:Mapped["Customer"]=relationship(
        back_populates="Buied_items"
    ) 



