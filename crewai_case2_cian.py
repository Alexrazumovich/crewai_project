from crewai import Agent, Task, Crew, Process
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")

reader=Agent(
role="Reader",
goal="Парсить HTML по ссылке и выбирать слова из кода.",
backstory="Эксперт по веб-скрапингу и парсингу, который специализируется на автоматизации извлечения слов и текстовой информации из HTML-кода по заданным URL.",
tools=[],

)
analyst=Agent(
    role="Price Analyst",
    goal="Анализировать статистику цен на квартиры в Екатеринбурге.",
    backstory="Эксперт по анализу статистики цен на квартиры в Екатеринбурге. Использует современные методы анализа для повышения точности прогнозов.",
    tools=[],
)
vizualizer=Agent(
    role="Price Vizualizer",
    goal="Визуализировать статистику цен на квартиры в Екатеринбурге.",
    backstory="Эксперт по визуализации статистики цен на квартиры в Екатеринбурге. Использует современные методы визуализации для повышения наглядности.",
    tools=[],
)
predictor=Agent(
    role="Price Predictor",
    goal="Разработать модель прогнозирования цен на квартиры в Екатеринбурге.",
    backstory="Эксперт по созданию модели прогнозирования цен на квартиры в Екатеринбурге. Использует современные методы анализа для повышения точности прогнозов.",
    tools=[],
)

task1=Task(
    description="Получить HTML-код сайта https://ekb.cian.ru/",
    expected_output="HTML-код сайта https://ekb.cian.ru/",
    agent=reader,
)
task2=Task(
    description="Распарсить HTML-код и извлечь статистику цен на квартиры в Екатеринбурге.",
    expected_output="Список слов из содержимого страницы.",
    agent=reader,
)
task3=Task(
    description="Анализировать статистику цен на квартиры в Екатеринбурге, выделить ключевые показатели и оценить их релевантность.",
    expected_output="Анализ статистики цен на квартиры в Екатеринбурге, выделение ключевых показателей и оценка их релевантности.",
    agent=analyst,
)
task4=Task(
    description="Визуализировать статистику цен на квартиры в Екатеринбурге.",
    expected_output="Визуализация статистики цен на квартиры в Екатеринбурге.",
    agent=vizualizer,
)
task5=Task(
    description="Разработать модель прогнозирования цен на квартиры в Екатеринбурге.",
    expected_output="Модель прогнозирования цен на квартиры в Екатеринбурге.",
    agent=predictor,
)
crew=Crew(
    agents=[reader, analyst, vizualizer, predictor],
    tasks=[task1, task2, task3, task4, task5],
    verbose=True,
    process=Process.sequential,
)
result=crew.kickoff()
print(result)
