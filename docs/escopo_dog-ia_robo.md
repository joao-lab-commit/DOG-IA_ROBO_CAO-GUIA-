# Escopo do Projeto DOG-IA

## Sobre o projeto
O DOG-IA é um robô cão-guia feito para ajudar pessoas com deficiência visual a se locomoverem sozinhas em ambientes urbanos, desviando de obstáculos e seguindo um trajeto seguro.

## Objetivo
Desenvolver e simular um robô que consiga navegar de forma autônoma, detectar obstáculos e avisar o usuário sobre o que está ao redor.

## Funcionalidades previstas
- Detecção de obstáculos com LiDAR
- Reconhecimento de objetos e pessoas com câmera RGB-D
- Navegação autônoma até um destino
- Desvio de obstáculos em tempo real
- Envio de status do sistema por tópicos do ROS 2

## Tecnologias
- ROS 2 Humble
- Gazebo (simulação)
- RViz2 (visualização dos sensores)
- Python (rclpy)
- OpenCV e cv_bridge
- Git e GitHub

## Etapas
1. Configuração do ambiente (ROS 2, Gazebo e RViz2)
2. Criação do workspace e do pacote `dog_ia_core`
3. Nó de validação do ambiente (`valida_ambiente`)
4. Modelo do robô e simulação no Gazebo
5. Leitura dos sensores e navegação

## Etapa atual
Etapas 1 e 2 concluídas: ambiente configurado e nó `valida_ambiente` publicando no tópico `dog_ia/status`.

## Integrantes
João Pedro Lima Nascimento - R.A.: 104675
Leandro Valido dos Santos - R.A.: 86461
Murilo Seike Sakaue - R.A.: 99238
Marco Aurelio - R.A.: 101692
Willian Gabriel da Costa - RA: 102155
Gustavo Hatagami Barros - RA: 105484

## Curso
Ciência da Computação, 6º semestre, UNIFECAF