from staticpipes.config import Config

from staticpipes.pipes.exclude_underscore_directories import PipeExcludeUnderscoreDirectories
from staticpipes.pipes.exclude_dot_directories import PipeExcludeDotDirectories
from staticpipes.pipes.copy import PipeCopy
from staticpipes.pipes.jinja2 import PipeJinja2

import os

config = Config(
    pipes = [
        PipeExcludeUnderscoreDirectories(),
        PipeExcludeDotDirectories(),
        PipeCopy(extensions=["css"]),
        PipeJinja2(extensions=["html"]),
    ],
    context={
    }
)

if __name__ == "__main__":
    from staticpipes.cli import cli
    cli(config, os.path.join(os.path.dirname(os.path.realpath(__file__))), "_site")

