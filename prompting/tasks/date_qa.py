from dataclasses import dataclass
from prompting.tasks import Task


@dataclass
class DateQuestionAnsweringTask(Task):
    reward_definition = [
        dict(name="rouge", ngram="rouge-l", metric="f", weight=1.0),
    ]

    def __init__(self, llm_pipeline, context, create_reference=True):
        self.context = context
        section = self.context["section"]
        year, _, *event = self.context["event"].split()
        self.context["event"] = " ".join(event)
        options = {'Births':' was born ', 'Deaths':' died ', 'Events':' '}
        query = self.context["event"].strip(".") + options[self.context["type"]] + 'on what date?'
        reference = self.context["date"] + ", " + year.strip()
        super().__init__(
            name="date-based question answering",
            desc="get help answering a question",
            goal="to get the answer to the following question",
            query=query,
            reference=reference,
            topic=self.context["event"],
            subtopic="",
            tags="",
            static_reference=True,
            static_query=True,
        )