# production-proof/cost_calculator.py
def calculate_rag_cost(daily_requests, tokens_per_request, cost_per_1k_tokens):
    monthly_cost = (daily_requests * tokens_per_request * cost_per_1k_tokens / 1000) * 30
    return monthly_cost

yandex_cost = calculate_rag_cost(1000, 500, 3)  # 1000 запросов/день, 500 токенов, 3 руб/1000
ollama_cost = 15000  # Сервер 32GB RAM

print(f"YandexGPT: {yandex_cost:,.0f} руб/мес")
print(f"Ollama: {ollama_cost:,.0f} руб/мес")
print(f"Экономия: {yandex_cost - ollama_cost:,.0f} руб/мес")