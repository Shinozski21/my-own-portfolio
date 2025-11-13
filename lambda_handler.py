import awsgi
from urllib.parse import parse_qs
from main import app


def _normalize_event(event):
	"""Convert API Gateway payloads into the structure awsgi expects."""
	normalized = dict(event)
	if normalized.get("version") == "2.0" and "httpMethod" not in normalized:
		http = normalized.get("requestContext", {}).get("http", {})
		normalized["httpMethod"] = http.get("method", "GET")
		normalized["path"] = normalized.get("rawPath", http.get("path", "/"))

		raw_query = normalized.get("rawQueryString", "")
		if raw_query and not normalized.get("queryStringParameters"):
			normalized["queryStringParameters"] = {
				key: values[-1]
				for key, values in parse_qs(raw_query, keep_blank_values=True).items()
			}

	normalized.setdefault("queryStringParameters", {})
	normalized.setdefault("headers", event.get("headers") or {})
	normalized.setdefault("body", event.get("body", ""))
	normalized.setdefault("isBase64Encoded", event.get("isBase64Encoded", False))

	if normalized.get("path") is None:
		normalized["path"] = "/"
	else:
		normalized["path"] = _to_wsgi_str(normalized["path"])

	return normalized


def _to_wsgi_str(value):
	"""Coerce Unicode paths into the latin-1 surrogate form WSGI expects."""
	if not isinstance(value, str):
		return value
	try:
		value.encode("latin-1")
	except UnicodeEncodeError:
		return value.encode("utf-8", "surrogatepass").decode("latin-1")
	return value


def handler(event, context):
	"""Entrypoint for AWS Lambda via API Gateway."""
	return awsgi.response(
		app,
		_normalize_event(event),
		context,
		base64_content_types={
			"application/pdf",
			"application/octet-stream",
			"application/font-woff",
			"application/font-woff2",
			"image/jpeg",
			"image/png",
			"image/gif",
			"image/webp",
			"image/svg+xml",
			"font/woff",
			"font/woff2",
		},
	)
