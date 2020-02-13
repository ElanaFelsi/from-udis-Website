class Report:
    def __init__(self, number):
        self.number = number
        self.parts = dict()

    def add_check(self, part, is_ok):
        self.parts[part] = is_ok

    def render(self):
        res = ""
        for k, v in self.parts.items():
            res += f"* {k}: {'OK' if v else 'Failed'}\n"
        res += "PASSED" if self.passed() else "NOT PASSED"
        return f"Results for car #{self.number}\n{res}"

    def passed(self):
        return all(self.parts.values())
