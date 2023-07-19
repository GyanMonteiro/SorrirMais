import sqlite3
from sqlite3 import Error


class Banco():
    def conecta_banco(self):
        self.conexao = sqlite3.connect('bancodedados.bd')
        self.sql = self.conexao.cursor()

    def desconecta_banco(self):
        self.conexao.close()

    def criar_tabela(self):
        self.conecta_banco()
        try:
            self.sql.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_funcionario TEXT,
                cpf_funcionario real,
                login_funcionario TEXT,
                password_funcionario TEXT,
                role_funcionario TEXT
            )
        ''')
            self.conexao.commit()
            print('Tabela criada com sucesso!')
            self.desconecta_banco()
        except Error:
            print('Ocorreu erro!', Error)
