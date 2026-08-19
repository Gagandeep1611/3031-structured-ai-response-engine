from pydantic import BaseModel


class Step(BaseModel):
    explanation: str
    output: str


class aws_services(BaseModel):
    name: str
    explanation: str


class AWSHelpResponse(BaseModel):
    services_included: list[aws_services]
    steps: list[Step]
    closing_notes: str
