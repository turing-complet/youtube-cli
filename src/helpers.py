import json
import os

import googleapiclient.discovery


def save(top, video_id, prefix=""):
    if prefix != "":
        prefix = f"{prefix}_"
    fname = f"{prefix}{video_id}.json"
    with open(fname, "w") as f:
        json.dump(top, f, indent=2)


def get_yt_client():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YOUTUBE_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )
    return youtube


YOUTUBE_CLIENT = get_yt_client()
