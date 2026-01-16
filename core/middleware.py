import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        # request-phase logic
        request.request_id = request.headers.get("X-Request-ID", "no-request-id")

        response = self.get_response(request)

        # response-phase logic
        ms = (time.time() - start) * 1000
        response["X-Response-Time-ms"] = f"{ms:.2f}"
        logger.info(
            "request_id=%s path=%s ms=%.2f",
            request.request_id,
            request.path,
            ms,
        )
        return response
