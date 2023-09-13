import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os"],
    "include_files": []
}

executables = [
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\coletarDadosDolar.py", base=None),
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\coletarDadosEuro.py", base=None),
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\coletarDadosBoi.py", base=None),
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\coletarDadosMadeira.py", base=None),
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\coletarDadosCarbono.py", base=None),
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\coletarDadosMilho.py", base=None),
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\coletarDadosSoja.py", base=None),
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\coletarDadosAgua.py", base=None),
    Executable(
        r"C:\Users\Wando\Desktop\ProjetoBMV\CotacaoUcs_v02_Diario\precificacaoDiariaUcsPlaniha.py", base=None),

    # Adicione mais Executables para outros scripts de coleta
]

setup(
    name="Coleta de Dados Diária",
    version="0.2",
    description="Scripts de Coleta de Dados",
    options={"build_exe": build_exe_options},
    executables=executables
)
