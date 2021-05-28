from states import link_down

class maquida_estados():
    """ 
    Declara um maquina de estados simples baseado na classe com um método pra utilizar como um handle de estados 
    """

    def __init__(self):
        """ Método construtor """

        # define estado inicial
        self.state = link_down()

    def on_event(self, event):
        """
        Este método varia de acordo com o estado,
        pois o evento é implementado em cada classe
        """

        self.state = self.state.on_event(event)


print('Happy Path')

dispositivo = maquida_estados()

dispositivo.on_event('interface_ok')
dispositivo.on_event('pacote_ok_recebido')
dispositivo.on_event('pacote_ok_recebido')
dispositivo.on_event('pacote_ok_recebido')

print('\nPath testando estados')
# -> estado 1 vai pro 2
dispositivo.on_event('interface_ok')
# -> estado 2 vai pro 1
dispositivo.on_event('interface_nok')
# -> estado 1 vai pro 2
dispositivo.on_event('interface_ok')

# -> estado 2 vai pro 3
dispositivo.on_event('pacote_ok_recebido')
# -> estado 3 vai pro 2
dispositivo.on_event('nao_recebeu_resposta')
# -> estado 2 vai pro 3
dispositivo.on_event('pacote_ok_recebido')

# -> estado 3 vai pro 4
dispositivo.on_event('pacote_ok_recebido')
# -> estado 4 vai pro 1
dispositivo.on_event('interface_nok')