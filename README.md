# FI-Comp Summary Data API 

# Summary
- /index.html --> HTML Page that downloads data and displays with some simple visulisations. 
- /main.py --> used to generate the openapi.json file.  
- /data -- > JSON formatted summary data (static asset).
- /docs --> Swagger page for HTML and JSON endpoints.


# Generation of openapi.json
- install ```python3 -mpip install uvicorn fastapi pydantic```
- run uvicorn main:app --reload
- 