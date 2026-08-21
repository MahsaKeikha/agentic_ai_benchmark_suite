from AGENTS import task_designer_agent,evaluator_agent,adversarial_agent,statistics_agent,reporting_agent
def run(ctx): return [a.run(ctx) for a in [task_designer_agent,evaluator_agent,adversarial_agent,statistics_agent,reporting_agent]]
