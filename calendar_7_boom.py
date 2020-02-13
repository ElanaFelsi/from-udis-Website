import calendar


class MyTextCalendar(calendar.TextCalendar):
    def formatday(self, day, weekday, width):
        """
        Returns a formatted day.
        """

        if day == 0:
            s = ''
        elif day % 7 == 0 or (day-7) % 10 == 0:
            s = '**'
        else:
            s = '%2i' % day
        return s.center(width)


c = MyTextCalendar()
result = c.formatmonth(2014, 5)
print(result)