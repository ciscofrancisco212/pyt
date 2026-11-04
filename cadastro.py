import sys
import json
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QListWidget, QMessageBox
)
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QTextDocument

ARQUIVO_DADOS = "clientes.json"


class JanelaCadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Cadastro de Clientes")
        self.setMinimumSize(450, 630)

        # Carrega dados salvos anteriormente
        self.clientes = self.carregar_clientes()

        self.init_ui()
        self.aplicar_estilo_css()
        self.atualizar_lista()

    def carregar_clientes(self):
        if os.path.exists(ARQUIVO_DADOS):
            try:
                with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def salvar_clientes(self):
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            json.dump(self.clientes, f, ensure_ascii=False, indent=4)

    def init_ui(self):
        # Widget central da janela
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal vertical
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(25, 25, 25, 25)
        layout_principal.setSpacing(12)

        # Título
        self.lbl_titulo = QLabel("Cadastro de Clientes")
        self.lbl_titulo.setObjectName("titulo")
        layout_principal.addWidget(self.lbl_titulo)

        # Campo Nome
        self.lbl_nome = QLabel("Nome do Cliente:")
        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Digite o nome completo...")
        layout_principal.addWidget(self.lbl_nome)
        layout_principal.addWidget(self.input_nome)

        # Campo Idade
        self.lbl_idade = QLabel("Idade:")
        self.input_idade = QLineEdit()
        self.input_idade.setPlaceholderText("Digite a idade...")
        layout_principal.addWidget(self.lbl_idade)
        layout_principal.addWidget(self.input_idade)

        # Botão Cadastrar
        self.btn_cadastrar = QPushButton("Cadastrar Cliente")
        self.btn_cadastrar.setObjectName("btnCadastrar")
        self.btn_cadastrar.clicked.connect(self.cadastrar_cliente)
        layout_principal.addWidget(self.btn_cadastrar)

        # Lista de Clientes Cadastrados
        self.lbl_lista = QLabel("Clientes Cadastrados:")
        layout_principal.addWidget(self.lbl_lista)

        self.lista_widget = QListWidget()
        layout_principal.addWidget(self.lista_widget)

        # Botão Imprimir Relatório
        self.btn_imprimir = QPushButton("Imprimir Relatório")
        self.btn_imprimir.setObjectName("btnImprimir")
        self.btn_imprimir.clicked.connect(self.imprimir_clientes)
        layout_principal.addWidget(self.btn_imprimir)

        # Botão Deletar Selecionado
        self.btn_deletar = QPushButton("Deletar Cliente Selecionado")
        self.btn_deletar.setObjectName("btnDeletar")
        self.btn_deletar.clicked.connect(self.deletar_cliente)
        layout_principal.addWidget(self.btn_deletar)

        central_widget.setLayout(layout_principal)

    def aplicar_estilo_css(self):
        # Estilo QSS (Estilo idêntico ao CSS da web)
        estilo = """
            QMainWindow {
                background-color: #f8fafc;
            }
            QLabel {
                color: #334155;
                font-size: 14px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-weight: 600;
            }
            QLabel#titulo {
                font-size: 22px;
                font-weight: bold;
                color: #1e293b;
                margin-bottom: 5px;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cbd5e1;
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 14px;
                color: #0f172a;
            }
            QLineEdit:focus {
                border: 2px solid #3b82f6;
                background-color: #ffffff;
            }
            QPushButton#btnCadastrar {
                background-color: #2563eb;
                color: white;
                font-size: 15px;
                font-weight: bold;
                border-radius: 8px;
                padding: 12px;
                margin-top: 5px;
            }
            QPushButton#btnCadastrar:hover {
                background-color: #1d4ed8;
            }
            QPushButton#btnCadastrar:pressed {
                background-color: #1e40af;
            }
            QListWidget {
                background-color: #ffffff;
                border: 1px solid #cbd5e1;
                border-radius: 8px;
                font-size: 14px;
                color: #334155;
                padding: 5px;
            }
            QPushButton#btnImprimir {
                background-color: #0d9488;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px;
                margin-top: 5px;
            }
            QPushButton#btnImprimir:hover {
                background-color: #0f766e;
            }
            QPushButton#btnImprimir:pressed {
                background-color: #115e59;
            }
            QPushButton#btnDeletar {
                background-color: #dc2626;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton#btnDeletar:hover {
                background-color: #b91c1c;
            }
            QPushButton#btnDeletar:pressed {
                background-color: #991b1b;
            }
        """
        self.setStyleSheet(estilo)

    def cadastrar_cliente(self):
        nome = self.input_nome.text().strip()
        idade_texto = self.input_idade.text().strip()

        if not nome:
            QMessageBox.warning(self, "Aviso", "O nome do cliente não pode estar vazio!")
            return

        try:
            idade = int(idade_texto)
        except ValueError:
            QMessageBox.warning(self, "Aviso", "Por favor, digite um número válido para a idade!")
            return

        self.clientes.append({"nome": nome, "idade": idade})
        self.salvar_clientes()

        self.input_nome.clear()
        self.input_idade.clear()
        self.atualizar_lista()

        QMessageBox.information(self, "Sucesso", f"Cliente {nome} cadastrado com sucesso!")

    def imprimir_clientes(self):
        if not self.clientes:
            QMessageBox.warning(self, "Aviso", "Não há clientes cadastrados para imprimir!")
            return

        # Cria uma página HTML limpa para formatar a impressão profissionalmente
        html_conteudo = """
        <html>
        <head>
            <style>
                body { font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; color: #1e293b; }
                h2 { text-align: center; color: #0f172a; margin-bottom: 25px; }
                table { width: 100%; border-collapse: collapse; }
                th, td { border: 1px solid #cbd5e1; padding: 12px; text-align: left; font-size: 14px; }
                th { background-color: #f1f5f9; color: #334155; font-weight: bold; }
                tr:nth-child(even) { background-color: #f8fafc; }
            </style>
        </head>
        <body>
            <h2>Relatório de Clientes Cadastrados</h2>
            <table>
                <tr>
                    <th style="width: 10%;">#</th>
                    <th style="width: 65%;">Nome do Cliente</th>
                    <th style="width: 25%;">Idade</th>
                </tr>
        """

        for i, cliente in enumerate(self.clientes, 1):
            html_conteudo += f"""
                <tr>
                    <td>{i}</td>
                    <td>{cliente['nome']}</td>
                    <td>{cliente['idade']} anos</td>
                </tr>
            """

        html_conteudo += """
            </table>
        </body>
        </html>
        """

        # Configurações de Impressão do PyQt
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            document = QTextDocument()
            document.setHtml(html_conteudo)
            document.print(printer)
            QMessageBox.information(self, "Sucesso", "Relatório enviado para impressora com sucesso!")

    def deletar_cliente(self):
        linha_selecionada = self.lista_widget.currentRow()

        if linha_selecionada < 0:
            QMessageBox.warning(self, "Aviso", "Por favor, selecione um cliente na lista para deletar!")
            return

        cliente_removido = self.clientes.pop(linha_selecionada)
        self.salvar_clientes()
        self.atualizar_lista()

        QMessageBox.information(self, "Sucesso", f"Cliente '{cliente_removido['nome']}' removido com sucesso!")

    def atualizar_lista(self):
        self.lista_widget.clear()
        for i, cliente in enumerate(self.clientes, 1):
            texto = f"{i}. Nome: {cliente['nome']} | Idade: {cliente['idade']} anos"
            self.lista_widget.addItem(texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaCadastro()
    janela.show()
    sys.exit(app.exec())