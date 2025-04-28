import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from bot import bot


def handler(request, context):
    match request["method"]:
        case "GET":
            return {
                "statusCode": 200,
                "body": '{"status":"online"}',
                "headers": {"Content-Type": "application/json"},
            }

        case "POST":
            headers = request.get("headers", {})
            response = bot.on_interaction(
                body=request.get("body", "{}"),
                signature=headers.get("x-signature-ed25519"),
                timestamp=headers.get("x-signature-timestamp"),
            )
            return {
                "statusCode": response.status_code,
                "body": response.body,
                "headers": dict(response.headers),
            }

        case _:
            return {
                "statusCode": 405,
                "body": '{"error":"Method not allowed"}',
                "headers": {"Content-Type": "application/json"},
            }
