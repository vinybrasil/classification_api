from uuid import uuid4

from pydantic import BaseModel, Field


class PayloadSchema(BaseModel):
    total_time_spent_on_website: float
    last_notable_activity_sms_sent: float
    lead_origin_lead_add_form: float
    what_matters_most_to_you_in_choosing_a_course_better_career_prospects: float
    occupation_working_professional: float
    what_matters_most_to_you_in_choosing_a_course_unknown: float
    total_visits: float
    last_activity_sms_sent: float
    page_views_per_visit: float
    last_activity_email_opened: float
    last_notable_activity_modified: float
    do_not_email: float
    specialization_unknown: float
    lead_source_olark_chat: float
    lead_source_direct_traffic: float


class Prediction(BaseModel):
    lead_score: int


class RequestSchema(BaseModel):
    request_id: str = Field(default_factory=lambda: str(uuid4()))
    lead_id: str
    payload: PayloadSchema


class ResponseSchema(BaseModel):
    request_id: str
    lead_id: str
    prediction: Prediction
