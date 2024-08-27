import sys
import os
from cx_Freeze import setup, Executable

arquivos = ['python.ico']

config = Executable(
    script='app.py',
    icon='python.ico'
)

setup(
    name='Gerador de senhas',
    version='1.0',
    description='Este programa gera senhas de acordo com as escolhas do usuário.',
    author='Carlos Rodrigues',
    options={'build_exe': {'include_files': arquivos}},
    executables=[config]
)
