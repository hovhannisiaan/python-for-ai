class Printer:
    def __init__(self):
        pass

    def __enter__(self):
        print("Printer started")
        return self

    def print_text(self, text):
        print(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Printer stopped")



with Printer() as p:
    p.print_text("Hello")
    p.print_text("Python")
