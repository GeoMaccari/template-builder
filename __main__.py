# -*- coding: utf-8 -*-
""" @author: Gabriel Maccari """

import sys

from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QIcon
from docx.opc.exceptions import PackageNotFoundError
from icecream import ic

from Model import Modelo
from View import Interface, caminho_dependencia
from Controller import Controlador

ic.configureOutput(prefix='LOG| ', includeContext=True)

TEMPLATE_ESTILOS = caminho_dependencia(r"appdata\template_estilos.docx")
JSON_COLUNAS = caminho_dependencia(r"appdata\config.json")


def erro_dependencia(arquivo, excecao) -> None:
    """ Mostra uma mensagem de erro para arquivos essenciais ausentes ou inválidos e encerra o programa. """
    ic(excecao)

    popup = QMessageBox(None)
    popup.setText(
        f"Erro ao acessar o arquivo:\n{arquivo}"
        f"\n\nRestaure o arquivo a partir do repositório e tente novamente."
    )
    popup.setWindowTitle("Erro")
    popup.setWindowIcon(QIcon(caminho_dependencia("appdata/icones/error.png")))
    popup.exec()

    sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    try:
        model = Modelo(TEMPLATE_ESTILOS, JSON_COLUNAS)
        view = Interface(model.colunas)
        controller = Controlador(model, view)

    except PackageNotFoundError as erro:
        erro_dependencia(TEMPLATE_ESTILOS, erro)

    except FileNotFoundError as erro:
        arquivo = getattr(erro, "filename", "arquivo desconhecido")
        erro_dependencia(arquivo, erro)

    app.exec()
