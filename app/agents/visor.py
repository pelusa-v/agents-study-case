import json
from .client import client
from ..utils.image_utils import function_metadata, get_text_from_image

class VisorAgent:

    _client = client
    _default_tools_choice = "auto"
    _default_model = "gpt-3.5-turbo"
    _default_query_message = {"role": "user", "content": None}
    _default_messages = [
        {"role": "system", "content": "You're an expert in reading images"}
    ]

    def __init__(self, *tools) -> None:
        self._tools = tools

    def query(self, content):
        self._default_query_message["content"] = content
        self._default_messages.append(self._default_query_message)

        print(self._default_messages)

        res = self._client.chat.completions.create(
            model=self._default_model,
            messages=self._default_messages,
            tools=[
                {
                    "type": "function",
                    "function": function_metadata
                }
            ],
            tool_choice=self._default_tools_choice
        )

        args = json.loads(res.choices[0].message.tool_calls[0].function.arguments)
        function_name = res.choices[0].message.tool_calls[0].function.name
        function_object = globals()[function_name]  # search function by name in all code

        print("--------")
        print(args)

        function_object(**args) # make dynamic

        # for c in res.choices:
        #     print(c.finish_reason)
        #     print(c.message)
        #     print(c.message.role)
        #     for t in c.message.tool_calls:
        #         print(t.function.arguments)
        #         print(t.function.name)

        return res        
