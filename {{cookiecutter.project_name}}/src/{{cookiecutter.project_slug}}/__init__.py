import os
from pkg_resources import get_distribution, DistributionNotFound

try:
    _dist = get_distribution('{{ cookiecutter.project_slug }}')

    # Normalize case for Windows systems
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)

    if not here.startswith(os.path.join(dist_loc, '{{ cookiecutter.project_slug }}')):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Version not found.'
else:
    __version__ = _dist.version
