from pydantic import BaseModel, Field,computed_field
from typing import Annotated,Literal

## take input data for prediction and validate it using pydantic
# Input : ['age', 'weight', 'height', 'income_lpa', 'smoker', 'city', 'occupation']
# Compute : ['income_lpa', 'occupation', 'bmi','age_group', 'lifestyle_risk', 'city_tier']

class user_input(BaseModel):
    age: Annotated[int,Field(...,description="Age of the person in years",gt=0,lt=120,examples=[25,45,60])]
    weight: Annotated[float,Field(...,description="Weight of the person in kg",gt=0,examples=[70.5,80.2])]
    height: Annotated[float,Field(...,description="Height of the person in m",gt=0,le=2.5,examples=[1.75,1.60])]
    income_lpa: Annotated[float,Field(...,description="Annual income of the person in lakhs per annum",gt=0,examples=[5.0,10.0])]
    smoker: Annotated[bool,Field(...,description="Whether the person is a smoker or not",examples=[True,False])]
    city: Annotated[str,Field(...,description="City of residence of the person",examples=["Mumbai","Delhi","Bangalore"])]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'],Field(...,description="Occupation of the person")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def age_group(self):
        if self.age < 25:
            return "Young"
        elif self.age < 45:
            return "Adult"
        elif self.age < 60:
            return "Middle-aged"
        else:
            return "Senior"
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        


    