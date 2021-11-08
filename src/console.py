import click

from .channel import get_channel_info
from .comments import get_comment_threads
from .helpers import save as _save, extract_video_id
from .videos import get_video


@click.group()
@click.option("--api-key", envvar="YOUTUBE_KEY")
@click.pass_context
def cli(ctx, api_key):
    ctx.obj = {"api_key": api_key}


@cli.command()
@click.option("--video-id", help="the video id")
@click.pass_context
def test(ctx, video_id):
    click.echo(f"Getting comments for {video_id=}, {ctx.obj['api_key']=}")


@cli.command()
@click.option("--video-id", help="the video id")
@click.option("--url", help="video url")
@click.option("--limit", type=int, help="approximate max comments")
@click.option("--replies", is_flag=True, help="include comment replies")
@click.option("--save", is_flag=True, help="save to file (default is stdout)")
def comments(video_id, url, limit, replies, save):
    video_id = extract_video_id(url, video_id)
    top = get_comment_threads(video_id, replies, limit)
    if save:
        _save(top, video_id)
    else:
        click.echo(top)


@cli.command()
@click.option("--video-id", help="the video id")
@click.option("--url", help="video url")
@click.option("--save", is_flag=True, help="save to file (default is stdout)")
def video(video_id, url, save):
    video_id = extract_video_id(url, video_id)
    details = get_video(video_id)
    if save:
        _save(details, video_id)
    else:
        click.echo(details)


@cli.command()
@click.option("--channel-id", help="channel id")
@click.option("--username", help="channel username")
def channel(channel_id, username):
    channel_info = get_channel_info(channel_id, username)
    click.echo(channel_info)
