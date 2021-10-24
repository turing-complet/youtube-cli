import click

from .comments import get_comment_threads
from .helpers import save as _save, extract_video_id
from .videos import get_video


@click.group()
@click.option("--api-key", envvar="YOUTUBE_KEY")
@click.pass_context
def cli(ctx, api_key):
    ctx.obj = {"api_key": api_key}


@click.command()
@click.option("--video-id", help="the video id")
@click.pass_context
def test(ctx, video_id):
    click.echo(f"Getting comments for {video_id=}, {ctx.obj['api_key']=}")


@click.command()
@click.option("--video-id", help="the video id")
@click.option("--url", help="video url")
@click.option("--save", is_flag=True)
def comments(video_id, url, save):
    video_id = extract_video_id(url, video_id)
    top = get_comment_threads(video_id)
    if save:
        _save(top, video_id)
    else:
        click.echo(top)


@click.command()
@click.option("--video-id", help="the video id")
@click.option("--url", help="video url")
@click.option("--save", is_flag=True)
def video(video_id, url, save):
    video_id = extract_video_id(url, video_id)
    details = get_video(video_id)
    if save:
        _save(details, video_id)
    else:
        click.echo(details)


cli.add_command(comments)
cli.add_command(video)
cli.add_command(test)
