code_review_system_promt = (
    "You are senior python developer, specialized on reviewing code"
)
code_review_user_promt = """
ROLE task constrains out

TASK:
    Review python code
CONSTRAINS:
    be specific and technical

CODE:
    def foo(x):
        if x == 1:
            return 1
        return x * foo(x - 1)
"""
