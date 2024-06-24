# Gerenciador_Manografias
Trabalho prático da  disciplina de Sistemas Distribuídos do curso de Sistemas de Informação da UFVJM-Campus Diamantina.
Certificação Digital no Trabalho Prático Gerenciador de Manográfia.
Certificação Digital e Chave Pública( linux ubuntu 20.04) 


             Tutorial Parte 1

Para instalar o OpenSSL em seu sistema, utilize o seguinte comando no terminal: 
         
          sudo apt-get install openssl

Geração da Chave Privada e do Certificado de Assinatura de Requisição (CSR):

Gere uma chave privada de 2048 bits com o comando:

openssl genrsa -out mysite.key 2048

Isso criará um arquivo chamado mysite.key contendo a chave privada.

Em seguida, gere o Certificado de Assinatura de Requisição (CSR) associado à chave privada:

          openssl req -new -key mysite.key -out mysite.csr

  Ao executar esse comando, será solicitado que você forneça informações relevantes, como país, estado, cidade, organização, etc. Preencha-as conforme apropriado.
     

   3. Geração de um Certificado Autoassinado:

       Agora, para criar um certificado autoassinado, utilize o seguinte comando:
      
openssl x509 -req -days 365 -in mysite.csr -signkey mysite.key -out mysite.crt

Este comando cria um certificado autoassinado válido por 365 dias, utilizando a chave privada (mysite.key) e o CSR (mysite.csr). O certificado resultante será armazenado em um arquivo chamado mysite.crt.


Lembre-se de que certificados autoassinados são adequados para ambientes de teste e desenvolvimento, mas em ambientes de produção, é recomendável obter um certificado assinado por uma autoridade certificadora confiável para garantir a autenticidade do seu site.



 Tutorial Parte 2
    
Configuração do Django para Execução com SSL:

Para executar seu aplicativo Django usando SSL, siga os passos abaixo, substituindo "/path/to/certificate.crt" pelo caminho onde está o certificado gerado e "/path/to/key.key" pelo caminho onde está a chave privada, ambos obtidos nos passos anteriores.
Ativação do Ambiente Virtual:
 Certifique-se de que seu ambiente virtual esteja ativado. Se você não tiver um ambiente virtual, é uma boa prática criar um para isolar as dependências do seu projeto. Ative-o usando: 

source env/bin/activate

Certifique-se de ter o pacote django-sslserver instalado em seu ambiente Django. Caso não tenha instalado, execute:

pip install django-sslserver

Adição ao INSTALLED_APPS em settings.py: Abra o arquivo settings.py no diretório do seu projeto Django e adicione 'sslserver' à lista INSTALLED_APPS. Certifique-se de adicionar a vírgula no final da linha anterior para evitar erros de sintaxe. A seção INSTALLED_APPS deve ficar assim:
    
                 INSTALLED_APPS = [
    # ... outras apps ...
    'sslserver',
]
Após seguir esses passos, seu projeto Django estará configurado para usar o django-sslserver. Certifique-se de ajustar os caminhos e nomes de diretórios conforme necessário para o seu projeto específico.
    
Agora, ao iniciar o servidor usando SSL, utilize o seguinte comando:

python manage.py runsslserver --certificate /path/to/certificate.crt --key /path/to/key.key

     Este comando iniciará o servidor Django e o configurará para aceitar conexões seguras usando o certificado e a chave privada fornecidos.

Quando você gerou seu certificado e chave privada usando os comandos OpenSSL mencionados anteriormente, você escolheu um local no sistema de arquivos para salvar esses arquivos. Vamos supor que você os salvou em um diretório chamado "/caminho/do/seu/diretorio".

Agora, ao executar o comando 
 
                 python manage.py runsslserver --certificate /path/to/certificate.crt --key /path/to/key.key

você precisa substituir "/path/to/certificate.crt" pelo caminho completo do arquivo do certificado que você gerou e "/path/to/key.key" pelo caminho completo do arquivo da chave privada que você gerou.

Lembre-se de ajustar "/caminho/do/seu/diretorio" de acordo com o local real onde você salvou seus arquivos de certificado e chave privada. Esses caminhos são específicos para a estrutura de diretórios do seu sistema. Certifique-se de fornecer o caminho exato para os arquivos correspondentes.



