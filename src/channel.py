from dataclasses import dataclass
from typing import Dict

from .helpers import YOUTUBE_CLIENT as YT


@dataclass
class ChannelInfo:
    channel_id: str
    video_count: int
    view_count: int
    subscriber_count: int
    playlists: Dict[str, str]

    @staticmethod
    def from_dict(resp):
        deets = resp["items"][0]
        vids = deets["contentDetails"]["relatedPlaylists"]
        vids = {k: v for k, v in vids.items() if v != ""}
        stats = deets["statistics"]
        return ChannelInfo(
            channel_id=deets["id"],
            video_count=int(stats["videoCount"]),
            view_count=int(stats["viewCount"]),
            subscriber_count=int(stats["subscriberCount"]),
            playlists=vids,
        )


def get_channel_info(channel_id=None, username=None):
    if channel_id is not None:
        req = YT.channels().list(
            part="id,snippet,contentDetails,statistics",
            id=channel_id,
        )
    elif username is not None:
        req = YT.channels().list(
            part="id,snippet,contentDetails,statistics",
            forUsername=username,
        )
    else:
        raise ValueError("Must supply either channel_id or username")

    resp = req.execute()
    # return resp
    return ChannelInfo.from_dict(resp)
