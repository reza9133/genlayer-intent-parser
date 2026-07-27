# v0.2.17
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class IntentParser(gl.Contract):
    total_intents: u256
    last_raw_intent: str
    last_parsed_action: str

    def __init__(self):
        self.total_intents = u256(0)
        self.last_raw_intent = ""
        self.last_parsed_action = "NONE"

    @gl.public.write
    def parse_intent(self, user_intent: str) -> str:
        prompt = f"""
        You are a Web3 Natural Language Intent Parser on GenLayer.
        Analyze the following user text and extract the intended blockchain action, parameters, and conditions.

        User Request:
        "{user_intent}"

        Respond strictly in valid JSON format with the following keys:
        - "action_type": string (e.g., "TRANSFER", "SWAP", "STAKE", or "UNKNOWN")
        - "recipient": string (extracted wallet address or ENS, or "NONE")
        - "amount_str": string (extracted token amount or "NONE")
        - "condition": string (any conditional logic like "if ETH > 3000" or "NONE")
        - "is_executable": boolean (true if intent has enough clear details to execute safely)
        """
        
        # Multi-validator consensus for parsing user intents safely
        res = gl.eq_principle.prompt_non_comparative(
            lambda: prompt,
            task="Parse user natural language into structured Web3 transaction intent",
            criteria="Must be valid JSON containing action_type, recipient, amount_str, condition, and is_executable."
        )
        
        parsed_result = str(res)
        self.last_raw_intent = user_intent
        self.last_parsed_action = parsed_result
        self.total_intents = self.total_intents + u256(1)
        
        return parsed_result

    @gl.public.view
    def get_last_parsed_intent(self) -> str:
        return self.last_parsed_action

    @gl.public.view
    def get_total_stats(self) -> u256:
        return self.total_intents
