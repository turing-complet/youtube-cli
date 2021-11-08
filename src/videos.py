from dataclasses import dataclass

from .helpers import YOUTUBE_CLIENT as YT


@dataclass
class Statistics:
    view_count: int
    comment_count: int

    @staticmethod
    def from_dict(stats):
        return Statistics(
            view_count=int(stats["viewCount"]),
            comment_count=int(stats["commentCount"]),
        )


@dataclass
class Video:
    video_id: str
    title: str
    statistics: Statistics
    # content_details: dict

    @staticmethod
    def from_dict(video):
        return Video(
            video_id=video["video_id"],
            title=video["title"],
            statistics=Statistics.from_dict(video["statistics"]),
            # content_details=video["contentDetails"],
        )

    def video_url(self):
        return f"https://www.youtube.com/watch?v={self.video_id}"


def get_video(video_id):
    req = YT.videos().list(part="snippet,contentDetails,statistics", id=video_id)
    resp = req.execute()
    result = {}
    body = resp["items"][0]
    result["video_id"] = body["id"]
    result["title"] = body["snippet"]["title"]
    result["statistics"] = body["statistics"]
    result["contentDetails"] = body["contentDetails"]
    return Video.from_dict(result)
