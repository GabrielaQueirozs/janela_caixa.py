import sys

# importar os componentes para a contrução da janela
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QTableWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QPixmap
# Contrução da classe janela com o nome de caixa

class Caixa(QWidget):
    # Criação do método _init_ que inicia a janela e exibe ela em tela 
    def __init__(self):
        super().__init__()

        # Definir a posição e o tamanho da tela
        self.setGeometry(0,30,1200,800)


        # Definir o título da nossa janela
        self.setWindowTitle("Caixa da loja")

        # Vamos criar as labels que representam as colunas esquerda e direita
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#87CEEB; font-size:15px}")
        # Label da direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#00BFFF}")

        #--------------Criar o conteúdo da coluda da esquerda---------------

        self.vlayout_esquerda = QVBoxLayout()
        # Vamos criar uma label para adicionar a logo na nossa loja
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("C:/Users/gabriela.qnunes/Documents/janela nova/foto2.png"))
         
        # Ajustar a label e a imagem para ficar do tamanho ideal

        self.logo_label.setScaledContents(True)
        self.logo_label.setFixedHeight(300)
        # Adicionar a label com a imagem na tela
        self.vlayout_esquerda.addWidget(self.logo_label) 


        # Vamos criar as labels e as linesEdits que ficarão na coluna da esquerda, dentro do layout vertical da esquerda
        
        self.codigo_produto_label = QLabel("Código do Produto:")
        self.codigo_produto_edit = QLineEdit()
        
        self.vlayout_esquerda.addWidget(self.codigo_produto_label)
        self.vlayout_esquerda.addWidget(self.codigo_produto_edit)

        self.nome_produto_label = QLabel("Nome do produto:")
        self.nome_produto_edit = QLineEdit()
        self.vlayout_esquerda.addWidget(self.nome_produto_label)
        self.vlayout_esquerda.addWidget(self.nome_produto_edit)

        self.descricao_produto_label = QLabel("Descrição do Produto:")
        self.descricao_produto_edit = QLineEdit()
        self.vlayout_esquerda.addWidget(self.descricao_produto_label)
        self.vlayout_esquerda.addWidget(self.descricao_produto_edit)



        # Criar a linha de Quantidade de Produtos
        self.quantidade_produto_label = QLabel("Quantidade de Produto:")
        self.quantidade_produto_edit = QLineEdit()
        self.vlayout_esquerda.addWidget(self.quantidade_produto_label)
        self.vlayout_esquerda.addWidget(self.quantidade_produto_edit)

        self.preco_produto_label = QLabel("Preço Unitário do produto:")
        self.preco_produto_edit = QLineEdit()
        self.vlayout_esquerda.addWidget(self.preco_produto_label)
        self.vlayout_esquerda.addWidget(self.preco_produto_edit)

        self.total_produto_label = QLabel("Sub Total:")
        self.total_produto_edit = QLineEdit()
        self.vlayout_esquerda.addWidget(self.total_produto_label)
        self.vlayout_esquerda.addWidget(self.total_produto_edit)


        # Adicionar o layout vertical da esquerda com todos os controles: label e lineEdit dentro da coluna da esquerda(label_coluna_esqueda)
        self.label_coluna_esquerda.setLayout(self.vlayout_esquerda) 



        #--------------------------------Controles da coluna da direita----------------------------
        self.vlayout_direita = QVBoxLayout()
        # Criar uma tabela ao lado e adicioanar na coluna da diretita ///// esta tabela terá nomes dos campos que estão do lado esquerdo

        #Colunas da tabela
        colunas = ["Cód.Produto", "Nome do produto", "Descrição", "Quantidade", "Preço Unitário","Sub Total"]
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setRowCount(10)
        self.vlayout_direita .addWidget(self.tabela)

        self.total_pagar_label = QLabel("Total a Pagar")
        self.total_pagar_edit = QLineEdit("0,00")
        self.vlayout_direita.addWidget(self.total_pagar_label)
        self.vlayout_direita.addWidget(self.total_pagar_edit)
 
        self.label_coluna_direita.setLayout(self.vlayout_direita)








 
        # Criar o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()

        # Vamos adicionar as colunas esquerda e direita do layout horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        # Adicinar o layout na tela 
        self.setLayout(self.h_layout)







app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()    









