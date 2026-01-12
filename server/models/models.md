from pydantic import BaseModel,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id: int
    items:List[str]
    quantities:Dict[str,int]

class BlogPost(BaseModel):
    title:str
    content:str
    image_url:Optional[str] =None

class Employee(BaseModel):
    emply_id:int
    name:str = Field(...,min_length=3,
                     max_length=50,
                     description="employee name"
                     examples="pritam Mondal"
                     
                     )
    department:Optional[str]= 'General'
    salary:float =Field(...,ge=10000)

class yser(BaseModel):
    username:str        


    @field_validator('username')     ##cutom validation
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("username must be 4 character !")
        return v
    


class SignupData(BaseModel):
    pasws:str
    confirm_pass:str    

    @model_validator(mode='after')
    def password_match(cls,values):
        if values.passws !=values.confirm_pass:
            raise ValueError("password donot match")
        return values
    



class Product(BaseModel):
    price:int
    quantity:int

    @computed_field
    @property
    def total_price(self)=>float:
        return self.price*self.quantity
      
           
class Booking_model(BaseModel):
    user_id:int
    room_id:int
    nights:int=Field(...,min>=1)
    rate_per_night:float
    @computed_field
    @property
    def total_amount(self)=>float:
        return self.nights*self.rate_per_night
    



class Address(BaseModel):
    street:str
    city:str
    postal_code:str



class travel_user(BaseModel):
    id:int
    name:str
    address:Address


class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None

#froward refferanceing 
Comment.model_rebuild()

address= Address(
    street="123 spmu",
    city="jaiput",
    postal_code="1001"
)

user=travel_user(
    id=1,
    name="Pritam",
    address=address


)


Comment=Comment(

    id=2,
    content="first comment",
    replies=[
        Comment(id=2,content="reply1"),
        Comment(id=3,content="2ndcomment")
    ]




)

