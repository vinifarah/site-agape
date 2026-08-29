# -*- coding: utf-8 -*-
"""
Servidor local — opcional.

O protótipo abre com duplo clique no index.html. Este script serve para
navegar por HTTP em vez de file://, o que deixa o comportamento mais próximo
do site publicado (cache, caminhos absolutos, ferramentas de desenvolvedor).

Uso:  python servir.py          (porta 5174)
      python servir.py 8080     (outra porta)

Lembrete: se você mexeu em conteudo.py, blocos.py ou build.py, rode
`python build.py` antes — este script só serve os arquivos, não os gera.
"""

import http.server
import os
import socketserver
import sys
import webbrowser

PORTA = int(sys.argv[1]) if len(sys.argv) > 1 else 5174
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class SemCache(http.server.SimpleHTTPRequestHandler):
    """Desliga o cache: editar o CSS e dar F5 mostra a mudança na hora."""

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def log_message(self, formato, *args):
        pass    # silencia o log de cada requisição de logo


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORTA), SemCache) as servidor:
        url = "http://localhost:%d/" % PORTA
        print("Protótipo Ágape (versão WordPress) em %s" % url)
        print("Ctrl+C para parar.")
        webbrowser.open(url)
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print("\nservidor encerrado")
