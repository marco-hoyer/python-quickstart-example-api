from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "python-quickstart-example-api"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on('argparse')
    project.depends_on('flask')
    project.depends_on('flask-restful')
    project.depends_on('ordereddict')
    project.set_property('install_dependencies_upgrade', True)