from airflow.models import Variable
from airflow.plugins_manager import AirflowPlugin


def tmp_path(ti, prefix=None):
    if prefix is None:
        prefix = Variable.get('tmp_path')

    key = '{}/{}/{:%Y%d%m%H%M%S}'.format(prefix,
                                         ti.dag_id,
                                         ti.execution_date)
    return key


class TmpPathPlugin(AirflowPlugin):
    name = "tmppath_plugin"
    hooks = []
    operators = []
    executors = []
    macros = [tmp_path]
    admin_views = []
    flask_blueprints = []
    menu_links = []
