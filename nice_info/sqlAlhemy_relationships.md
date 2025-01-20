Как контролировать поведение relationship?

SQLAlchemy позволяет настраивать стратегию загрузки relationship с помощью параметра lazy:

    lazy='select' (по умолчанию): Связанные объекты загружаются отдельным запросом при первом обращении.

lesson_task = relationship("LessonTask", lazy="select")

lazy='joined': Связанные объекты загружаются вместе с основным запросом с использованием JOIN.

lesson_task = relationship("LessonTask", lazy="joined")

lazy='subquery': Связанные объекты загружаются с использованием подзапроса.

lesson_task = relationship("LessonTask", lazy="subquery")

lazy='noload': Связанные объекты никогда не загружаются автоматически, даже при обращении.

lesson_task = relationship("LessonTask", lazy="noload")

lazy='selectin': Использует стратегию "select in" для загрузки связанных объектов отдельным запросом.

    lesson_task = relationship("LessonTask", lazy="selectin")

Итог

    При запросе Lesson по id, SQLAlchemy не выполняет лишний запрос для lesson_task, если вы не обращаетесь к этому свойству напрямую.
    Если вы хотите полностью избежать загрузки связей, настройте lazy="noload".
    Если вы хотите загрузить всё сразу, настройте lazy="joined" или используйте joinedload в запросах.

Таким образом, поведение зависит от вашей настройки relationship и от того, как вы запрашиваете данные.
