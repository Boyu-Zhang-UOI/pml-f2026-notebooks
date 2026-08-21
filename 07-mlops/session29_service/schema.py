# What the service will and will not accept.

from typing import Literal

from pydantic import BaseModel, Field


class Customer(BaseModel):
    model_config = {"extra": "forbid"}          # an unexpected field is an error

    tenure_months: float = Field(ge=0, le=600)
    monthly_charges: float | None = Field(default=None, ge=0, le=1000)
    support_calls: float = Field(ge=0, le=100)
    plan: Literal["basic", "plus", "premium"]
    region: Literal["north", "south", "coast"]


class Prediction(BaseModel):
    churn_probability: float = Field(ge=0, le=1)
    churn: bool
    threshold: float
    model_version: str
