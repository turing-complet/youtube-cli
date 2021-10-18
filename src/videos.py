from .helpers import YOUTUBE_CLIENT as YT


def get_video(video_id):
    req = YT.videos().list(part="snippet,contentDetails,statistics", id=video_id)
    resp = req.execute()
    result = {}
    body = resp["items"][0]
    result["title"] = body["snippet"]["title"]
    result["statistics"] = body["statistics"]
    result["contentDetails"] = body["contentDetails"]
    return result


def get_channel_videos(channel_id):
    pass
