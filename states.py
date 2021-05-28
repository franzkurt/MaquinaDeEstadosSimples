class Estado():
    def __init__(self):
        print ("estado atual: " + str(self))

    def __str__(self):
        return self.__class__.__name__

# estado 1
class link_down(Estado):

    def on_event(self, event):

        if event == 'interface_ok':
            return send_start()

        print ("estado atual: " + str(self))
        return self

# estado 2
class send_start(Estado):

    def on_event(self, event):
        if event == 'pacote_ok_recebido':
            return receive_start()
        elif event == 'interface_nok':
            return link_down()
        return self

# estado 3
class receive_start(Estado):

    def on_event(self, event):
        if event == 'pacote_ok_recebido':
            return link_ok()
        elif event == 'interface_nok':
            return link_down()
        elif event == 'nao_recebeu_resposta':
            return send_start()
        return self

# estado 4
class link_ok(Estado):

    def on_event(self, event):
        if event == 'interface_nok':
            return link_down()
        elif event == 'pacote_nok_recebido' or event == 'nao_recebeu_resposta':
            return send_start()

        return self
