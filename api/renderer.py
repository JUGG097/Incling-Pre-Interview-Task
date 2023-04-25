from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json

class APIRenderer(JSONRenderer):
    # media_type = 'text/plain'
    # media_type = 'application/json'
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        response = {"success": True, "data": data}
        if not str(status_code).startswith("2"):
            response = {"success": True, "message": ""}
            response["success"] = False
            response["message"] = None
            try:
                response["message"] = data["detail"]
            except KeyError:
                response["data"] = data
        data = response
        return json.dumps(data)