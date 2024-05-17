import joblib
import numpy as np

from app.schemas import Prediction, RequestSchema, ResponseSchema
from app.utils import scale_numerical_variables


def predict_request(request):
    model = joblib.load("app/model.z")
    payload_dict = dict(request.payload)
    payload_array = np.array(list(payload_dict.values())).reshape(1, -1)
    return model.predict_proba(payload_array)[0][0] * 1000


def prediction_pipeline(request: RequestSchema) -> ResponseSchema:

    request = scale_numerical_variables(request)
    score = predict_request(request)
    prediction = Prediction(lead_score=int(np.floor(score)))

    response = ResponseSchema(
        request_id=request.request_id, lead_id=request.lead_id, prediction=prediction
    )

    return response
