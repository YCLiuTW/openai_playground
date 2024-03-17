# openai_playground
A demo repo for Generative AI recommender!

## Lanuch Backend
1.) change parameter OPENAI_KEY(with your openai key) in backend/llm_router.py. (MUST Support GhatGPT4)
```sh
cd openai_playground
docker-compose up -d --build
```

## Lanuch Frontend

```sh
cd openai_playground
jupyter-notebook
```
And open demo.ipynb in browser.