# CriptografiaBasica
Criptografia com Diffie-Hellman

Interceptação R1:

<img width="917" alt="image" src="https://github.com/GuiCSantiago/CriptografiaBasica/assets/76591370/b7b285c6-bd28-4d70-ba2d-a443307794c2">

Interceptação R2:

<img width="921" alt="image" src="https://github.com/GuiCSantiago/CriptografiaBasica/assets/76591370/9304bede-8af6-4b9e-85f9-3cc483b54057">

Data Sent:

<img width="922" alt="image" src="https://github.com/GuiCSantiago/CriptografiaBasica/assets/76591370/9da13084-083b-48ac-af90-ac173181e579">

Data Received:

<img width="919" alt="image" src="https://github.com/GuiCSantiago/CriptografiaBasica/assets/76591370/9af81003-4ba0-4da1-a273-ad495cd4deca">

Cli do Cliente:

<img width="422" alt="image" src="https://github.com/GuiCSantiago/CriptografiaBasica/assets/76591370/400d762e-b679-4c97-8dd2-dc3f449fc414">

## Início da Comunicação: 
O Cliente e servidor estabelecem uma conexão TCP. O cliente e o servidor têm seus próprios parâmetros privados (X para o cliente, Y para o servidor), que são números escolhidos aleatoriamente.

## Troca de Chaves Diffie-Hellman:

O cliente calcula r1 usando a base G elevada à sua chave privada X, módulo N, e envia r1 para o servidor.
O servidor recebe r1, calcula r2 da mesma forma (usando G elevado à sua chave privada Y, módulo N) e envia r2 de volta para o cliente.
Tanto o cliente quanto o servidor calculam a chave compartilhada usando os valores recebidos (r2 no caso do cliente, r1 no caso do servidor) elevados à sua própria chave privada, módulo N. Isso resulta na mesma chave compartilhada em ambos os lados devido às propriedades matemáticas do Diffie-Hellman.

## Comunicação Criptografada:

O cliente então criptografa uma mensagem usando a chave compartilhada (alterando o valor ASCII de cada letra pela adição da chave) e envia a mensagem criptografada para o servidor.
O servidor descriptografa a mensagem recebida, converte-a para maiúsculas, criptografa a mensagem novamente usando a mesma chave, e envia de volta para o cliente.
O cliente descriptografa a mensagem recebida para obter a versão em maiúsculas da mensagem original.
Aplicação do Diffie-Hellman
A aplicação do algoritmo Diffie-Hellman (DH) aqui serve para estabelecer uma chave compartilhada entre o cliente e o servidor de maneira segura, mesmo através de um canal inseguro. O DH é baseado na dificuldade de resolver o logaritmo discreto em um campo finito, o que torna computacionalmente inviável para um observador calcular a chave compartilhada, mesmo conhecendo G, N, r1, e r2.

## Importância
### Segurança: 
Permite que as duas partes estabeleçam uma chave secreta compartilhada sem nunca terem que enviá-la diretamente uma à outra. Isso é fundamental para comunicações seguras, pois mesmo que um invasor consiga interceptar os dados trocados, sem a chave compartilhada, ele não pode descriptografar a comunicação.
### Criptografia e Descriptografia: 
A chave compartilhada é usada para modificar os dados enviados entre cliente e servidor, garantindo que apenas as partes com a chave possam entender o conteúdo da mensagem.
Este método é amplamente utilizado em vários protocolos de segurança na internet, como TLS/SSL, para estabelecer comunicações seguras.
