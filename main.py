from datetime import datetime

class Mensagem:
    def __init__(self, mensagem, arquivo, formato):
        self.mensagem = mensagem
        self.arquivo = arquivo
        self.formato = formato
        self.data_envio = datetime.now()

    def enviar(self):
        raise NotImplementedError("Método 'enviar' deve ser implementado nas subclasses")

class MensagemTexto(Mensagem):
    def enviar(self):
        print(f"@Marisilva: {self.mensagem}")
        print(f"Data de Envio: {self.data_envio}")

class MensagemVideo(Mensagem):
    def __init__(self, mensagem, arquivo, formato, duracao):
        super().__init__(mensagem, arquivo, formato)
        self.duracao = duracao

    def enviar(self):
        print(f"Enviando Vídeo: {self.mensagem}")
        print(f"Formato: {self.formato}")
        print(f"Duração: {self.duracao} segundos")
        print(f"Data de Envio: {self.data_envio}")

class MensagemFoto(Mensagem):
    def enviar(self):
        print(f"@Mabisanto: Tudo sim e com voce? Veja que foto linda eu tirei: {self.mensagem}")
        print(f"Formato: {self.formato}")
        print(f"Data de Envio: {self.data_envio}")

class MensagemArquivo(Mensagem):
    def enviar(self):
        print(f"@Mabisanto: {self.mensagem}")
        print(f"Formato: {self.formato}")
        print(f"Data de Envio: {self.data_envio}")

mensagem_texto = MensagemTexto("Olá, como você está? Segue o video da nossa viagem", None, None)
mensagem_texto.enviar()

mensagem_video = MensagemVideo("Vídeo da Viagem", "video.mp4", "MP4", 60)
mensagem_video.enviar()

mensagem_foto = MensagemFoto( "foto.jpg", "JPEG")
mensagem_foto.enviar()

mensagem_arquivo = MensagemArquivo("Segue o roteiro para nossa proxima voagem:", "roteiro.pdf", "PDF")
mensagem_arquivo.enviar()
