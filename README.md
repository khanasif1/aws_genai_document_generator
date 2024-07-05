# AWS GenAI generate document using bedrock RAG

***

## Setup environment

```
 python3 -m venv venv   

 source venv/bin/activate  

 pip install -r requirements.txt  

```

## Run application

```

 cd ./legal-document-generator 

 streamlit run app.py  
 
 ```

 ## Prompt

 ```

Create a Consultancy Services Agreement with below details, use all content as in knowledge base samples, fill General Terms from sample document 
Principal Name - Revantage 
Principal Address -  Revantage, Suite 612, Level 2, 150 Castlereagh Street, Melb Vic 2000
Consultant Name - John Boggs
Consultant Address - ABN: Not eligible		
Address: 1 Bogg Drive, Bogg City, Australia
Commencement Date - 25 March 2026
Service Fee - $10000
Payment Terms -  14 days from receipt 
Required Insurance - 10,000,000 to 90,000,000 
Required Notice - 1 month

```