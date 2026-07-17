# 🦔 AI Studio

> **Next Generation Open Source AI IDE**

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-Ruff-black.svg)](https://github.com/astral-sh/ruff)
[![Typing](https://img.shields.io/badge/typing-mypy-blue.svg)](https://mypy-lang.org/)
[![Tests](https://img.shields.io/badge/tests-pytest-success.svg)](https://pytest.org/)
[![Status](https://img.shields.io/badge/status-development-orange)]()

---

## 📖 О проекте

**AI Studio** — современная модульная среда разработки с поддержкой искусственного интеллекта.

Цель проекта — объединить редактор кода, интеллектуальных AI-агентов, управление проектами и работу с несколькими LLM-провайдерами в единой платформе.

Проект разрабатывается как полностью открытое программное обеспечение (Open Source) с расширяемой архитектурой, системой плагинов и возможностью локального и облачного использования.

---

# ✨ Основные возможности

## 🤖 AI-провайдеры

Поддержка нескольких моделей одновременно.

- OpenAI
- Anthropic Claude
- Google Gemini
- Ollama
- OpenRouter
- LM Studio
- локальные модели

---

## 🦔 AI Manager

Главный координатор системы —

# 🦔 Ёжик

Ёжик управляет всеми специализированными агентами.

---

## 👥 Команда агентов

| Агент | Назначение |
|--------|------------|
| 🦔 Ёжик | AI Manager |
| 🏛 Atlas | Software Architect |
| 💻 Nova | Senior Programmer |
| 🛡 Sentinel | Code Reviewer |
| 🧪 Pulse | QA Engineer |
| 📚 Echo | Project Memory |
| ⚙ Forge | DevOps Engineer |

Каждый агент имеет собственный:

- системный промпт;
- настройки модели;
- память;
- инструменты;
- историю диалогов.

---

# 🏗 Архитектура

Проект построен по принципам **Clean Architecture**.

```text
                   UI
                    │
            Application
                    │
               Domain
                    │
          Infrastructure

──────────────────────────────────

                 Core

        Service Container
             Event Bus
             Scheduler
        Module Manager
        Plugin Manager
              Kernel
```

---

# 📂 Структура проекта

```text
AI-Studio/

├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── development/
│   ├── roadmap.md
│   └── decisions/
│
├── scripts/
│
├── src/
│   └── ai_studio/
│
│       ├── application/
│       ├── config/
│       ├── core/
│       ├── domain/
│       ├── infrastructure/
│       ├── plugins/
│       ├── providers/
│       ├── shared/
│       ├── ui/
│       ├── workspace/
│       ├── agents/
│       ├── __main__.py
│       ├── bootstrap.py
│       └── version.py
│
├── tests/
│
├── pyproject.toml
├── README.md
├── LICENSE
└── CHANGELOG.md
```

---

# ⚙ Требования

- Python 3.12+
- Git
- pip

---

# 🚀 Установка

```bash
git clone https://github.com/zeroyu97-gif/AI-Studio.git

cd AI-Studio

python -m venv .venv
```

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Установка

```bash
pip install -e ".[dev]"
```

---

# ▶ Запуск

```bash
python -m ai_studio
```

---

# 🧪 Проверка качества

Проверка форматирования

```bash
ruff check .
```

Автоформатирование

```bash
ruff format .
```

Типизация

```bash
mypy src
```

Тесты

```bash
pytest
```

Полная проверка

```bash
ruff check . && mypy src && pytest
```

---

# 🔌 Система плагинов

AI Studio поддерживает динамическую загрузку плагинов.

Каждый плагин содержит:

- manifest
- настройки
- зависимости
- команды
- инструменты
- UI
- AI Agents

---

# 🤖 Провайдеры AI

Все модели работают через единый интерфейс.

```text
BaseProvider

├── OpenAIProvider
├── GeminiProvider
├── ClaudeProvider
├── OllamaProvider
├── LMStudioProvider
└── OpenRouterProvider
```

Замена модели не требует изменения остального кода.

---

# 📁 Workspace

Каждый проект имеет собственное рабочее пространство.

Поддерживаются:

- индексация файлов;
- поиск;
- embeddings;
- RAG;
- память проекта;
- история изменений.

---

# 📚 Документация

```
docs/

architecture/

api/

development/

tutorials/

roadmap/

decisions/
```

---

# 🛣 Roadmap

## Phase 1

- Repository Foundation

## Phase 2

- Core Runtime

## Phase 3

- Providers

## Phase 4

- Workspace

## Phase 5

- UI

## Phase 6

- AI Agents

## Phase 7

- Plugin SDK

## Phase 8

- Stable Release

---

# 🧩 Принципы проекта

- Clean Architecture
- Dependency Injection
- Event Driven
- Plugin First
- Strong Typing
- Test Driven Development
- SOLID
- Open Source

---

# 🤝 Участие в разработке

Мы приветствуем вклад сообщества.

1. Fork репозитория.
2. Создайте новую ветку.
3. Внесите изменения.
4. Добавьте тесты.
5. Создайте Pull Request.

---

# 📄 Лицензия

Проект распространяется по лицензии **MIT**.

Подробнее см. файл **LICENSE**.

---

# ❤️ Благодарности

Спасибо всем участникам проекта и Open Source сообществу за идеи, тестирование и развитие AI Studio.

---

# 🌟 AI Studio

> **Open Source AI IDE нового поколения**

Главный агент проекта:

# 🦔 Ёжик

*"Один менеджер. Команда специализированных AI-агентов. Единая интеллектуальная среда разработки."*
