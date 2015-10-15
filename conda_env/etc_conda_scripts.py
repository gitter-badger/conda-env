from __future__ import print_function
from .print_env import print_env
import os
import sys



def write_activate_deactivate(env, prefix):
    '''Write activate/deactivate environment variable/aliases scripts'''
    if not env.environment and not env.aliases:
        return

    # Create directories
    conda_dir = os.path.join(prefix, 'etc', 'conda')
    activate_dir = os.path.join(conda_dir, 'activate.d')
    deactivate_dir = os.path.join(conda_dir, 'deactivate.d')
    for directory in [conda_dir, activate_dir, deactivate_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Copy print_env.py
    import shutil
    shutil.copyfile(
        os.path.join(os.path.dirname(__file__), 'print_env.py'),
        os.path.join(conda_dir, 'print_env.py'),
    )

    if sys.platform == 'win32':
        ext = '.bat'
    else:
        ext = '.sh'

    with open(os.path.join(activate_dir, '_activate' + ext), 'w') as activate:
        activate.write(print_env('activate', env.environment, env.aliases))

    with open(os.path.join(deactivate_dir, '_deactivate' + ext), 'w') as deactivate:
        deactivate.write(print_env('deactivate', env.environment, env.aliases))
