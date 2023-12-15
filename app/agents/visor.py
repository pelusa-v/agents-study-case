from .client import client

class VisorAgent:

    _client = client
    _tools = []
    _default_tools_choice = "auto"
    _default_model = "gpt-3.5-turbo"
    _default_query_message = {"role": "user", "content": None},
    _default_messages = [
        {"role": "system", "content": "You're an expert in reading images"},
    ]

    def __init__(self, *tools) -> None:
        self._tools = tools

    def query(self, content):
        self._default_query_message["content"] = content
        self._default_messages.append(self._default_query_message)

        res = self._client.chat.completions.create(
            model=self._default_model,
            messages=self._default_messages,
            tools=self._tools,
            tool_choice=self._default_tools_choice
        )

        return res
    
    # def validate

