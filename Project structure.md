# Project structure

```bash
/ml-architect-basics
├── README.md # Главный дашборд с бизнес-метриками
├── docs/
│ ├── adr/ # Архитектурные решения (главное!)
│ │ ├── 001-perceptron-vs-transformer.md
│ │ ├── 002-precision-vs-cost.md
│ │ └── 003-lora-for-enterprise.md
│ └── concept-diagrams/ # Схемы вместо кода
│ ├── ml-evolution.png # Как персептрон → трансформер
│ └── rag-metrics.png # Связь метрик и бизнеса
├── core-concepts/ # Код ТОЛЬКО для доказательства понимания
│ ├── perceptron.py # Персептрон без библиотек (Week 1)
│ ├── lora_simulator.py # LoRA своими руками (Week 3)
│ └── cost_calculator.py # Расчёт cost RAG (Week 4)
└── production-proof/ # Доказательство production-мышления
├── metrics_demo.py # Как считать precision@k (Week 2)
└── latency_benchmark.py # Нагрузочное тестирование (Week 4)
```

---
