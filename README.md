# Kubernetes-EKS-Lab
**Contexto**:
  - Subir aplicação demo utilizando ArgoCD para sicronização deste repositorio com cluster Kubernetes.
  - Aplicar novos requerimentos em cima do modelo base

# Etapas do Lab
- Clone este repositorio e crie uma pasta para sua App a partir da pasta **modelo**. Incialmente o template serviceAccount.yaml **não** deve ser copiado.
- Criar arquivo de Application do ArgoCD seguindo o modelo do **portela-app.yaml**
- Além do modelo base, os seguintes requerimentos devem ser implementados nos templates seguindo a estrutura do Helm chart:
  - Deployment
    - variavel de ambiente como nome de usuario
    - readness probe/liveness prob no path /health
    - requests e limits para o container
  - Service
    - tipo ClusterIP
- Após deploy dos objetos acima, realizar teste na aplicação:
  -   Chamada no localhost/ e localhost/generate
  -   Check de logs do Pod
  -   Incialmente a chamada host/generate deve falhar por falta de permissão, para corrigir isso devemos criar um role e uma service account.
- Criar role usando o OIDC do cluster e atrelando a uma Service Account
  - Criar Service Account usando o **template** na pasta **modelo**
  - Criar nova Role como Trusted Entity sendo Web Identity
  -  Selecionar o arn OIDC do cluster e 'sts' como Audience durante
  -  Atrelar permissões necessarias para Secret Manager e criar role
  -  Editar o Trust Relationship da Role para apontar para service account.
  -  Desconmentar annotation no template de Service Account e ajustar nome da role previamente criada
  - Adicionar referencia para Service Account no Deployment
- Realizer push das alterações, sincronizar Argo e Validar aplicação