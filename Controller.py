# -*- coding: utf-8 -*-
""" @author: Gabriel Maccari """

from icecream import ic


class Controlador:
    def __init__(self, modelo, interface):
        super().__init__()

        # Atributos do controlador
        self.modelo = modelo
        self.interface = interface
        self.caminho_caderneta = None

        # Conecta os botões de abrir arquivo e gerar a caderneta às funções
        self.interface.botao_abrir_arquivo.clicked.connect(self.botao_abrir_arquivo_clicado)
        self.interface.botao_gerar_nova_caderneta.clicked.connect(self.botao_gerar_nova_caderneta_clicado)

        # Define a função a ser conectada aos botões de status das colunas
        self.interface.funcao_botoes_status = self.icone_status_clicado

        self.interface.checkbox_continuar_caderneta.clicked.connect(self.checkbox_continuar_caderneta_clicada)

        self.interface.show()

    def botao_abrir_arquivo_clicado(self):
        """
        Chama a função para abrir a tabela no controlador. Caso um arquivo seja aberto com sucesso, atualiza o
        rotulo_arquivo com o nome do arquivo selecionado e chama o método checar_colunas para atualizar os ícones de
        status.
        :returns: Nada.
        """
        ic()

        try:
            # arquivo_aberto, num_pontos = False, "-"   # Eu removi isso e A PRINCÍPIO não quebrou nada :)
            caminho = self.interface.mostrar_dialogo_arquivo(
                "Selecione uma tabela contendo os dados de entrada.",
                "Pasta de trabalho do Excel (*.xlsx);;Pasta de trabalho habilitada para macro do Excel (*.xlsm);;"
            )
            if caminho == "":
                return

            arquivo_aberto, num_pontos = self.modelo.abrir_tabela(caminho)

            if not arquivo_aberto:
                return

            self.interface.atualizar_arquivo(caminho, num_pontos, self.modelo.df["Ponto"])
            self.modelo.abrir_aba_listas(caminho)
            self.checar_colunas()

            if "nan" in self.modelo.df.columns:
                self.interface.mostrar_popup(
                    "Atenção! Existem colunas com nomes inválidos na tabela que podem causar erros ou "
                    "anomalias no funcionamento da ferramenta. Verifique se as fórmulas presentes nas células de "
                    "cabeçalho das colunas de estruturas (colunas S a AL) não foram comprometidas. Isso geralmente "
                    "ocorre ao recortar e colar células na aba de Listas ao preencher as estruturas."
                )

        except Exception as exception:
            self.interface.mostrar_popup(f"{exception}", "erro")
            ic(exception)

    def checar_colunas(self):
        """
        Chama a função do controlador para checar se cada coluna está no formato especificado. Atualiza os botões de
        status conforme o resultado. Se todas as colunas estiverem OK, habilita o botão para gerar o template.
        :returns: Nada.
        """
        ic()

        status_colunas = self.modelo.checar_colunas()
        self.interface.atualizar_status_colunas(status_colunas)
        self.interface.definir_estado_botao_gerar(all(stts == "ok" for stts in status_colunas))

    def icone_status_clicado(self, coluna: str, status: str):
        """
        Chama a função do controlador para identificar os problemas na coluna e mostra os resultados em uma popup.
        :param coluna: A coluna a ser verificada.
        :param status: O status da coluna ("ok", "faltando", "problemas", "nulos" ou "dominio").
        :returns: Nada.
        """
        ic(coluna, status)

        try:
            localizar_problemas = {
                "coluna_faltando": lambda coluna_faltando: [],
                "fora_de_formato": self.modelo.localizar_problemas_formato,
                "celulas_vazias": self.modelo.localizar_celulas_vazias,
                "valores_nao_permitidos": self.modelo.localizar_problemas_dominio,
                "fora_do_intervalo": self.modelo.localizar_problemas_intervalo,
                "valores_repetidos": self.modelo.localizar_valores_repetidos
            }

            if status not in localizar_problemas:
                raise Exception(f"O status informado não foi reconhecido: {status}")

            indices_problemas = localizar_problemas[status](coluna)

            msg = self.modelo.montar_msg_problemas(status, coluna, indices_problemas)
            self.interface.mostrar_popup(msg)

        except Exception as exception:
            self.interface.mostrar_popup(f"{exception}", "erro")
            ic(exception)

    def checkbox_continuar_caderneta_clicada(self):
        """
        Permite ao usuário selecionar uma caderneta pré-existente para ser continuada.
        :returns: Nada.
        """
        ic()

        try:
            continuar = self.interface.checkbox_continuar_caderneta.isChecked()

            if continuar:
                self.interface.marcar_folha_rosto(False)

                caminho = self.interface.mostrar_dialogo_arquivo(
                    "Selecione a caderneta a ser continuada",
                    "Documento do Word (*.docx);;",
                    "abrir"
                )

                if not caminho:
                    self.interface.definir_checkbox_continuar(False)
                    self.interface.marcar_folha_rosto(True)
                    continuar = False
                    self.caminho_caderneta = None
                else:
                    self.caminho_caderneta = caminho
            else:
                self.caminho_caderneta = None

            self.interface.atualizar_estado_continuar_caderneta(continuar)
        except Exception as exception:
            self.interface.mostrar_popup(f"{exception}", "erro")
            ic(exception)

    def botao_gerar_nova_caderneta_clicado(self):
        """
        Chama as funções do controlador para gerar a caderneta e exportá-la.
        :returns: Nada.
        """
        ic()
        caminho_saida = None

        self.interface.mostrar_cursor_espera(True)

        try:
            montar_folha_de_rosto = self.interface.checkbox_folha_rosto.isChecked()
            montar_folhas_semestre = self.interface.checkbox_folhas_semestre.isChecked()
            continuar_caderneta = self.caminho_caderneta
            ponto_inicio = self.interface.combobox_ponto_inicio.currentText()
            indice_ponto_inicio = self.modelo.df.index[self.modelo.df["Ponto"] == ponto_inicio][0]

            self.modelo.gerar_caderneta(
                montar_folha_de_rosto, montar_folhas_semestre, indice_ponto_inicio, continuar_caderneta
            )

            self.interface.mostrar_cursor_espera(False)

            caminho_saida = self.interface.mostrar_dialogo_arquivo(
                "Salvar caderneta", "Documento do Word (*.docx)", modo="salvar"
            )
            if caminho_saida != "":
                self.modelo.salvar_caderneta(caminho_saida)
                self.interface.mostrar_popup("Caderneta criada com sucesso!")

        except PermissionError as exception:
            self.interface.mostrar_cursor_espera(False)
            self.interface.mostrar_popup(
                f"Erro ao salvar a caderneta. Verifique se o arquivo {caminho_saida} não está aberto em outro"
                f" programa e se você possui privilégios para salvar na pasta selecionada.", "erro"
            )
            ic(exception)
        except Exception as exception:
            self.interface.mostrar_cursor_espera(False)
            self.interface.mostrar_popup(f"{exception}", "erro")
            ic(exception)

