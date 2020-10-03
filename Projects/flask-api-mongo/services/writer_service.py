from database.models.writer import Writers


class WriterService:
    @staticmethod
    def store(data):
        writer = Writers(**data)
        writer.save()

    @staticmethod
    def all():
        writers = Writers.objects().to_json()
        return writers
