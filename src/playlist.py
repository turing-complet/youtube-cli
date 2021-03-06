from .helpers import YOUTUBE_CLIENT as YT
from .videos import get_video, Video

# TODO: set max_results to video_count from channel


def get_playlist(playlist_id, max_results=100):
    req = YT.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=max_results,
    )
    resp = req.execute()
    video_ids = [item["snippet"]["resourceId"]["videoId"] for item in resp["items"]]
    videos = [get_video(vid) for vid in video_ids]
    return sorted(videos, key=lambda x: x.statistics.view_count, reverse=True)
