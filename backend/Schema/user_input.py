from pydantic import BaseModel, Field, computed_field
from typing import Annotated

class UserInput(BaseModel):
    age : Annotated[int, Field(..., lt=100, gt=0, description='Age of the Defendant')]
    juv_fel_count : Annotated[int, Field(..., description='number of felonies committed as a juvenile (serious crimes)')]
    juv_misd_count : Annotated[int, Field(..., description='misdemeanors as a juvenile (minor crimes)')]
    juv_other_count : Annotated[int, Field(..., description="other juvenile offenses that don't fit felony/misdemeanor")]
    priors_count : Annotated[int, Field(..., description='total prior criminal charges as an adult before this case')]
    charge_degree	: Annotated[str, Field(..., description='severity of current charge')]
    c_days_from_compas : Annotated[int, Field(..., description='days between the arrest/charge and when COMPAS was administered. Measures how quickly they were screened')]

    @computed_field
    @property
    def age_cat(self) -> str:
        if self.age < 25:
            return 'Young'
        elif self.age > 45:
            return 'Senior'
        else:
            return 'Adult'
        
    @computed_field
    @property
    def c_charge_degree(self) -> int :
        if self.charge_degree == 'F1':
            return 13
        elif self.charge_degree == 'F2':
            return 12
        elif self.charge_degree == 'F3':
            return 11
        elif self.charge_degree == 'F5':
            return 10
        elif self.charge_degree == 'F6':
            return 9
        elif self.charge_degree == 'F7':
            return 8
        elif self.charge_degree == 'TCX':
            return 7
        elif self.charge_degree == 'M1':
            return 6
        elif self.charge_degree == 'M2':
            return 5
        elif self.charge_degree == 'MO3':
            return 4
        elif self.charge_degree == 'CO3':
            return 3
        elif self.charge_degree == 'CT':
            return 2
        elif self.charge_degree == 'NI0':
            return 1
        else:
            return 0