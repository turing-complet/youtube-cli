import json
import os
from urllib.parse import urlparse, parse_qs

import googleapiclient.discovery


def save(top, video_id, prefix=""):
    if prefix != "":
        prefix = f"{prefix}_"
    fname = f"{prefix}{video_id}.json"
    with open(fname, "w") as f:
        json.dump(top, f, ensure_ascii=False, indent=2)


def extract_video_id(url=None, video_id=None):
    if video_id is not None:
        return video_id
    if url is not None:
        u = urlparse(url)
        q = parse_qs(u.query)
        if "v" in q:
            return q["v"][0]
    raise ValueError(f"No video found in {url=}, {video_id=}")


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
