import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        #Criando a janela
        layout = [
            [sg.Text("Quais as medidas da folha?", size=(25, 0), font=('Any 16'))],
            [sg.Radio('225 x 275 ', "RADIO1", default=True, key="225", font=('Any 12'))],
            [sg.Radio('230 x 280', "RADIO1", default=False, key="230", font=('Any 12'))],
            [sg.Text("Quantidade Embalada:", size=(20, 0), font=('Any 16')),
             sg.Input(size=(15, 0), key="qtd_embalada")],
            [sg.Text("Largura do jumbo:", size=(20, 0), font=('Any 16')), sg.Input(size=(15, 0), key="metragem_jumbo")],
            [sg.Text()],
            [sg.Text("Metragem puxada nos jumbos:", size=(25, 0), font=('Any 16'))],
            [sg.Text("1º jumbo:", size=(20, 0), font=('Any 16')),
             sg.Input("0", size=(15, 0), key="metragem_puxada")],
            [sg.Text("(Deixe zero caso não tenha utilizado outros jumbos)", size=(45, 0), font=('Any 10'))],
            [sg.Text("2º jumbo:", size=(20, 0), font=('Any 16')), sg.Input("0", size=(15, 0), key="segundo_puxada")],
            [sg.Text("3º jumbo:", size=(20, 0), font=('Any 16')), sg.Input("0", size=(15, 0), key="terceiro_puxada")],
            [sg.Text("4º jumbo:", size=(20, 0), font=('Any 16')), sg.Input("0", size=(15, 0), key="quarto_puxada")],
            [sg.Text("5º jumbo:", size=(20, 0), font=('Any 16')), sg.Input("0", size=(15, 0), key="quinto_puxada")],
            [sg.Text("6º jumbo:", size=(20, 0), font=('Any 16')), sg.Input("0", size=(15, 0), key="sexto_puxada")],
            [sg.Button("Calcular", font=('Any 16')),
             sg.Text("Desenvolvido por Thiago Carvalho. Versão: 3.1", size=(30, 0), font=('Any 8'))]
        ]
        janela = sg.Window("Calculadora de Waste", layout)
        eventos, valores = janela.Read()
        while True:
            #Executa ao apertar o botão calcular
            if eventos == "Calcular":
                try:
                    testes = valores["225"]
                    if testes == True:
                        medida_folha = 0.0618
                    else:
                        medida_folha = 0.0644
                    print(medida_folha)
                    qtd_embalada = valores["qtd_embalada"]
                    metragem_puxada = valores["metragem_puxada"]
                    metragem_jumbo = valores["metragem_jumbo"]
                    segundo_jumbo = valores["segundo_puxada"]
                    terceiro_jumbo = valores["terceiro_puxada"]
                    quarto_jumbo = valores["quarto_puxada"]
                    quinto_jumbo = valores["quinto_puxada"]
                    sexto_jumbo = valores["sexto_puxada"]

                    print(metragem_puxada)
                    print(qtd_embalada, metragem_jumbo, metragem_puxada)
                    metragem_puxada = int(metragem_puxada) + int(segundo_jumbo) + int(terceiro_jumbo) + int(quarto_jumbo) + int(quinto_jumbo) + int(sexto_jumbo)
                    print(qtd_embalada, metragem_jumbo, metragem_puxada)
                    metragem_emb = float(medida_folha) * float(qtd_embalada)
                    metragem_jumbo = float(metragem_jumbo) * 0.001
                    m2_puxado = float(metragem_jumbo) * float(metragem_puxada)
                    sobra = m2_puxado - metragem_emb
                    waste = (sobra / m2_puxado) * 100

                    if waste < 0:
                        waste = 0
                        sg.popup("O desperdício total é de: 0%", "Ou alguma informação foi digitada incorretamente.", font=('Any 24'))
                        janela.Close()
                        self.__init__()
                        break
                    else:
                        sg.popup("O desperdício total é de: " + str(int(sobra)) + "m²",
                                 "A porcentacegem é de: " + str(float(format(waste, '.1f'))) + "%", font=('Any 24'))
                        janela.Close()
                        self.__init__()
                        break

                    break
                except:
                    sg.popup("Ocorreu um erro, talvez você não tenha digitado os valores", font=('Any 16'))
                    janela.Close()
                    self.__init__()
                    break
            if eventos == sg.WIN_CLOSED:
                print("fechando janela")
                janela.Close()
                break


print("iniciando")
TelaPython()
#código para criação do executável
# pyinstaller --onefile -w waste.py
