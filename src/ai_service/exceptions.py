class LLMError(Exception):
    pass
    

class EmptyLLMOutputError(LLMError):
    pass
    
    
class LLMStructuredOutputError(LLMError):
    def __init__(self, message: str, raw_output: str, user_prompt: str):
        super().__init__(message)
        self.raw_output = raw_output