from models.File import File


class GetCardController:
    def __init__(self):
        pass

    @classmethod
    def run(cls, payload):
        file = File()
        return {
            'source': file.get_source(),
            'tags': file.get_tags(),
            'content':file.get_content()
        }
