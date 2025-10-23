from pydantic import BaseModel, Field, field_validator


class Package(BaseModel):
    width: float = Field(description="Width of the package in centimeters")
    height: float = Field(description="Height of the package in centimeters")
    length: float = Field(description="Length of the package in centimeters")
    mass: float = Field(description="Mass of the package in kilograms")

    @field_validator("width", "height", "length", "mass")
    @classmethod
    def must_be_positive(cls, v, info):
        if v <= 0:
            raise ValueError(f"{info.field_name} must be greater than 0")
        return v

    @property
    def volume(self) -> float:
        return self.width * self.height * self.length

    @property
    def is_bulky(self) -> bool:
        return (
            self.volume >= 1000000
            or self.width >= 150
            or self.height >= 150
            or self.length >= 150
        )

    @property
    def is_heavy(self) -> bool:
        return self.mass >= 20
