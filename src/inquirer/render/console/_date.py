from inquirer.render.console.base import BaseConsoleRender
from datetime import date
from datetime import timedelta


class Date(BaseConsoleRender):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current = self._current_index()
    
    def _current_index(self):
        return 0
    
    def get_options(self):
        first = date.today().replace(day=1)
        first -= timedelta(days=first.weekday())

        # TODO: Render calendar month view properly

        return [
            (
                f" 1  2  {self.theme.List.selection_color}3{self.theme.List.unselected_color}  4  5  6  7",
                self.theme.List.unselected_color,
                ""
            ),
        ]