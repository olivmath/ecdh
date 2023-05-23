# Criptografia Assimétrica com Diffie-Hellman: Simplificando a Segurança!

Eu sei que vc ama matemática tanto quanto eu e se tem um matemática massa é a tal da "Criptografia de Assimétrica com Curvas Elípticas”.

Imagine o seguinte problema:

1. Alice criptografa uma mensagem com sua senha e a envia para Bob.
2. Como Alice pode enviar a senha para Bob sem que ela seja interceptada?

O algoritmo de Diffie-Hellman resolve esse problema com facilidade, e a mágica está na criptografia assimétrica.

Na Criptografia de Chaves Assimétricas, os usuários possuem duas chaves: uma privada (senha) e uma pública (como um endereço de e-mail). Dessa forma, é possível compartilhar a chave pública (como um endereço de e-mail) para que todos a vejam, sem que alguém consiga acessar a chave privada (senha).

Vamos ver como o Diffie-Hellman funciona,Primeiro, criamos as chaves:

########## PYTHON ########## 
# Parâmetros
p = 23
g = 5

# Chave privada de Alice
alice_private_key = 6

# Chave privada de Bob
bob_private_key = 15
########## PYTHON ########## 

Agora, vamos gerar as chaves públicas:

########## PYTHON ########## 
# Chave pública de Alice
alice_public_key = (g ** alice_private_key) % p

# Chave pública de Bob
bob_public_key = (g ** bob_private_key) % p
########## PYTHON ########## 

Com as chaves geradas, Alice e Bob podem trocá-las de forma segura (como um email).

Mas aqui está a MateMágica: mesmo que alguém intercepte as chaves públicas, é extremamente difícil para essa pessoa descobrir as chaves privadas (senha)!

O algoritmo de Diffie-Hellman permite que Alice e Bob calculem a chave compartilhada (senha compartilhada):

########## PYTHON ########## 
# Chave compartilhada de Alice
alice_shared_key = (bob_public_key ** alice_private_key) % p

# Chave compartilhada de Bob
bob_shared_key = (alice_public_key ** bob_private_key) % p
########## PYTHON ########## 

No final, Alice e Bob têm a mesma chave compartilhada (senha), que pode ser usada para criptografar e descriptografar mensagens sem que ninguém mais consiga entender.

Vou deixar o link para meu repositório onde tem um exemplo mais completo dessa implementação.

**🚨 AVISO **
- ISSO É UM EXEMPLO DIDÁTICO
- Não use isso em produção mano, por favor mano
- Eu não usei números seguros, precisaria de primos muito maiores como  2^127 - 1
- Não usei proteção contra ataque de força bruta
- Não tentei garantir autenticidade

#python #cryptography #security #mathematic