code_review_system_promt = (
    "You are senior python developer, specialized on reviewing code"
)

def create_code_review_user_prompt(user_code: str):
    code_review_user_promt = """
    TASK:
        Review python code
    CONSTRAINS:
        - Be specific and technical
        - Do not give generic advice
        
    CODE:
        
    """
    return code_review_user_promt + user_code