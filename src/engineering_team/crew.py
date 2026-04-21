from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class EngineeringTeam():
    """EngineeringTeam crew"""

    # 1. Aapka Local unlimited server
    local_llm = LLM(
        model="ollama/llama3.1",
        base_url="http://localhost:11434"
    )

    # --- Agents ---
    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['engineering_lead'],
            llm=self.local_llm, # <--- Changed here
            verbose=True
        )

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engineer'],
            llm=self.local_llm, # <--- Changed here
            verbose=True
        )

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engineer'],
            llm=self.local_llm, # <--- Changed here
            verbose=True
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer'],
            llm=self.local_llm, # <--- Changed here
            verbose=True
        )

    @agent
    def devops_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['devops_engineer'],
            llm=self.local_llm, # <--- Changed here
            verbose=True
        )

    @agent
    def security_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['security_engineer'],
            llm=self.local_llm, # <--- Changed here
            verbose=True
        )

    @agent
    def data_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['data_engineer'],
            llm=self.local_llm, # <--- Changed here
            verbose=True
        )

    # --- Tasks ---
    @task
    def technical_planning_task(self) -> Task:
        return Task(config=self.tasks_config['technical_planning_task'])

    @task
    def backend_development_task(self) -> Task:
        return Task(config=self.tasks_config['backend_development_task'])

    @task
    def frontend_development_task(self) -> Task:
        return Task(config=self.tasks_config['frontend_development_task'])

    @task
    def quality_assurance_task(self) -> Task:
        return Task(config=self.tasks_config['quality_assurance_task'])

    @task
    def devops_infrastructure_task(self) -> Task:
        return Task(config=self.tasks_config['devops_infrastructure_task'])

    @task
    def security_review_task(self) -> Task:
        return Task(config=self.tasks_config['security_review_task'])

    @task
    def data_engineering_task(self) -> Task:
        return Task(config=self.tasks_config['data_engineering_task'])

    @task
    def final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_report_task'],
            output_file='engineering_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EngineeringTeam crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )