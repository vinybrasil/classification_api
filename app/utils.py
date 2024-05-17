import joblib
import numpy as np


def scale_numerical_variables(request):
    variables_to_scale = {}
    variables_to_scale["total_visits"] = request.payload.total_visits
    variables_to_scale["total_time_spent_on_website"] = (
        request.payload.total_time_spent_on_website
    )
    variables_to_scale["page_views_per_visit"] = request.payload.page_views_per_visit

    scaler = joblib.load("app/standard_scaler.z")
    scaled_variables = scaler.transform(
        np.array(list(variables_to_scale.values())).reshape(1, -1)
    )
    request.payload.total_time_spent_on_website = scaled_variables[0][0]
    request.payload.total_visits = scaled_variables[0][1]
    request.payload.page_views_per_visit = scaled_variables[0][2]
    return request
