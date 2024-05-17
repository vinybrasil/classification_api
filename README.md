# API de classificação usando Scikit-Learn, FastAPI e Docker

A API serve para classificar um dataset que vende cursos online para profissionais da insdústria, sendo que o mesmo está disponível [aqui](https://www.kaggle.com/datasets/amritachatterjee09/lead-scoring-dataset).
A ETL está disponível em notebooks/data_cleaning e a modelagem em notebooks/data_modelling. 


## Como usar

Buildar a imagem: 
```bash
docker build -t lead:latest .
```

Rodar ela:
```bash
docker run -p 8000:8000 lead:latest
```
Rota da requisição:
```
POST /api/v1/predict
```


Body da requisição:
```json
{
    "lead_id": "7927b2df-8bba-4d29-b9a2-b6e0beafe620",
    "payload": {
            "total_time_spent_on_website": 869.0,
            "last_notable_activity_sms_sent": 1.0,
            "lead_origin_lead_add_form": 0.0,
            "what_matters_most_to_you_in_choosing_a_course_better_career_prospects": 0.0,
            "occupation_working_professional": 0.0,
            "what_matters_most_to_you_in_choosing_a_course_unknown": 1.0,
            "total_visits": 9.0,
            "last_activity_sms_sent": 1.0,
            "page_views_per_visit": 4.5,
            "last_activity_email_opened": 0.0,
            "last_notable_activity_modified": 0.0,
            "do_not_email": 0.0,
            "specialization_unknown": 0.0,
            "lead_source_olark_chat": 0.0,
            "lead_source_direct_traffic": 0.0}
}
```
Payload de resposta:
```json
{
    "request_id": "7cbfe52c-970c-4411-a81b-20be81a6cf04",
    "lead_id": "7927b2df-8bba-4d29-b9a2-b6e0beafe620",
    "prediction": {
        "lead_score": 346
    }
}
```

## TODO 
Aqui estão listadas as necessidades hipotéticas para se possa ser viável usar este modelo em produção.

### Em relação à limpeza dos dados:
- Usar técnicas como KNN ou Decision Tree para imputar os dados faltantes em Asymmetrique Activity Index, Asymmetrique Profile Index, Asymmetrique Activity Score, Asymmetrique Profile Score uma vez que são variáveis com ordem
- Testar técnicas para imputar as variáveis numéricas, desde as simples como imputação por média/moda/mediana ou técnicas
mais complexas como até regressão linear
- Automatizar a ETL caso seja de responsabilidade dessa API (ou o CRM a faria)

### EDA
- Estudo das distribuições dos dados mais profundamente (exemplo: total_visits seguem uma distribuição Poisson) com o fitdistplus do R
- Limpeza de outliers/uso dos mesmos
- Estudo das correlações das variáveis
- Estudo de transformações (ex: usar a transformada Z em alguma variável)
- Estudo do threshold da função que agrega os valores das variáveis categóricas

### Modelagem
- Testar outros modelos com o PyCaret (talvez um CatBoost performe melhor, por exemplo)
- Utilizar as métricas alinhadas com a necessidade da empresa (usar o Mathew Correlation Coeficient dependendo da necessidade do Negócio)
- Otimizar os hiperparâmetros

### API 
- Carregar o modelo e o scaler no início da API (@app.onstartup)
- Usar injeção de dependência para que o fluxo fique menos complexo na hora de colocar no
banco de dados
- Usar o logging para gerar os log
- Error Handling
- Verificação da entrada (evitar ataques como SQLInjection com o lead_id, por exemplo)
- (Swagger)[https://fastapi.tiangolo.com/features/] e documentação da API

### Deploy (supondo um deploy na AWS)
- Adaptar o entrypoint para um lambda_handler
- Mudar a imagem do Docker para aws-lambda-python
- Conexão com banco de dados que permita futuras análises (DynamoDb)
- Criação de uma Feature Store para treinamento futuro de modelos
- Criar um script Terraform para ter sempre a mesma arquitetura independente do ambiente (DEV, QA, PROD)
- Criar um script de CI/CD no github 

### Monitoramento 
- Usar uma ferramenta que captura os logs para acompanhar em real-time (como [Datadog](https://docs.datadoghq.com/integrations/guide/aws-terraform-setup/))
- Acompanhamento das métricas do modelo com uma ferramenta como o PowerBI para 
evitar o Concept Drift
    - Caso aconteça, retreinar o modelo



