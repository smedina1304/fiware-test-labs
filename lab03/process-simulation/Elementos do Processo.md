# Elementos do Fluxo do Processo

## Elementos & Atributos:
1. **TANK**

	*Sensores:*
		- **LEVEL** - Percentual de ocupação do tanque (NIVEL).
		- **LEVEL.HIGH** - Sensor de alerta de nível alto (tipo on/off)
		- **LEVEL.LOW** - Sensor de alerta de nível baixo (tipo on/off)
		- **LITERS** - Quantidade em litros no tanque.
		- **TEMPERATURE** - Temperatura em C° do Material no tanque.

	*Status:*
		- **WAITING** - Indica que o tanque está com material e aguardando.
		- **AVAILABLE** - Indica que o tanque está liberado para uso no processo.
		- **FILLING** - Indica que o tanque está recebendo material.
		- **COOLING** - Indica que o tanque está acima da temperatura limite para o processo e ficará circulando para o resfriador até estar dentro da temperatura esperada.
		- **TRANSFER** - Indica que o processo está tirando material do tanque e enviando para próxima etapa do processo.
		- **CLEANING** - Indica que o tanque está em processo de limpeza.
		- **BLOCKED**  - Indica que o tanque está bloqueado aguardando ou em manutenção.

2. **VALVE**

	*Sensores:*
		- **POSITION** - Posição da válvula (aberta/fechada).

	*Status:*
		- **CLOSED** - Indica o posição como **FECHADA**.
		- **OPENED** - Indica o posição como **ABERTA**.


3. **PUMP**

	*Sensores:*
		- **OPERATION** - Estado de operação da bomba (ON/OFF).

	*Status:*
		- **OFF** - Indica o estado como **DESLIGADO** para o bombeamento.
		- **ON**  - Indica o estado como **LIGADO** para o bombeamento.


4. **COOLER**

	*Sensores:*
		- **TEMPERATURE** - Temperatura em C° do Material na saída do resfriador.

	*Status:*
		- **WAITING** - Indica que o resfriador está aguardando e sem utilização.
		- **COOLING** - Indica que o resfriador está em uso.
