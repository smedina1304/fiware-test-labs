# Elementos do Fluxo do Processo

## Elementos & Atributos:
1. **TANQUE**

	*Sensores:*
		- **NIVEL** - Percentual de ocupação do tanque.
		- **NIVEL.A** - Sensor de alerta de nível alto (tipo on/off)
		- **NIVEL.B** - Sensor de alerta de nível baixo (tipo on/off)
		- **LITROS** - Quantidade em litros no tanque.
		- **TEMPERATURA** - Temperatura  em C° do Material no tanque.

	*Status:*
		- **DISPONIVEL** - Indica que o tanque está liberado para uso no processo.
		- **ENCHENDO** - Indica que o tanque está recebendo material.
		- **AGUARDANDO** - Indica que o tanque está com material e aguardando.
		- **RESFRIANDO** - Indica que o tanque está acima da temperatura limite para o processo e ficará circulando para o resfriador até estar dentro da temperatura esperada.
		- **ESVAZIANDO** - Indica que o processo está tirando material do tanque e enviando para próxima etapa do processo.
		- **LIMPEZA** - Indica que o tanque está em processo de limpeza.
		- **BLOQUEIO** - Indica que o tanque está bloqueado aguardando ou em manutenção.

2. **VALVULA**

	*Status:*
		- **ABERTA** - Indica o estado como **ON** para a situação como aberta.
		- **FECHADA** - Indica o estado como **OFF** para a situação como fechada.

3. **BOMBA**

	*Status:*
		- **LIGADA** - Indica o estado como **ON** para a situação como ligada.
		- **DESLIGADA** - Indica o estado como **OFF** para a situação como desligada.

4. **RESFRIADOR**

	*Sensores:*
		- **TEMPERATURA** - Temperatura  em C° do Material na saída do resfriador.

	*Status:*
		- **RESFRIANDO** - Indica que o resfriador está em uso.
		- **AGUARDANDO** - Indica que o resfriador está aguardando e sem utilização.
