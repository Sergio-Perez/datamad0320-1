import os
import dotenv
dotenv.load_dotenv()
import sentry_sdk
from sentry_sdk import capture_exception

SENTRY_DSN=os.getenv("SENTRY_DSN")
sentry_sdk.init(SENTRY_DSN)


def captureError(fn):
    def wrapper(*args,**kwargs):
        try:
            fn(*args,**kwargs)
        except Exception as e:
            print(e)
            capture_exception(e)
            raise(e)
    return wrapper


@captureError
def main():
    raise ValueError("BIEEEEN")
    

main()