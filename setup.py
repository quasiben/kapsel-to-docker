import os
from setuptools import setup, find_packages
import versioneer


def get_data_files(path, extra_suffixes=None, check_suffix=True):
    data_files = []
    root = path

    suffix_list = ["py", "sls", "conf", "txt", "yaml", "repo"]
    if extra_suffixes is not None:
        suffix_list.extend(extra_suffixes)

    for path, dirs, files in os.walk(root):
        for fs in files:
            if check_suffix:
                if not fs.endswith(tuple(suffix_list)):
                    continue
                install_path = os.sep.join(path.split(os.sep)[1:])
                data_files.append(os.path.join(install_path, fs))
    return data_files


setup(name="k2d",
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description="Kapsel to Docker utility",
      url="https://github.com/quasiben/k2d",
      maintainer="Continuum Analytics",
      maintainer_email="ben.zaitlen@continuum.io",
      license="Enterprise",
      packages=find_packages(),
      zip_safe=False,
      entry_points="""
        [console_scripts]
        k2d=k2d.cli:start
      """,
      )
