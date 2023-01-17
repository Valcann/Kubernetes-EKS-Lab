# Kubernetes-EKS-Lab
Contexto:
  - Subir aplicação demo utilizando ArgoCD para sicronização deste repositorio com cluster Kubernetes.
  - Utilizar componenete Istio previamente instalado no cluster para permitir comunicação externa com a aplicação
  - Aplicar novos requerimentos em cima do modelo base

# Etapas do Lab
- Clone este repositorio e crie uma pasta para sua App a partir da pasta **modelo**
- Além do modelo base, os seguintes requerimentos devem ser implementados seguindo a estrutura do Helm chart:
  - Deployment
    - variavel de ambiente como nome de usuario
    - readness probe/liveness prob no path /health
    - requests e limits para o container
  - Service
    - tipo ClusterIP
  - Istio Ingress
    - configurar Gateway
    - configurar virtualService
- Após deploy dos objetos acima, realizar teste na aplicação:
  -   Chamada no host/ e host/generate
  -   Check de logs do Pod
  -   Incialmente a chamada host/generate deve falha por falta de permissão, para corrigir isso devemos criar um role e uma service account.
- Criar role usando o OIDC do cluster e atrelando a uma Service Account
  - 
  - Service Account
    - Atrelar IAM Role
    - Atrelar service account ao deployment
  - Criar role usando o OIDC do cluster como Trusted Relationship e ajustar para uso com Service Account