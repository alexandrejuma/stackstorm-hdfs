from lib.base_action import HDFSAction


class ListHDFS(HDFSAction):

    def __init__(self, config):
        super(ListHDFS, self).__init__(config=config)
        self.config = config

    def run(self, directory, file_status=False, **kwargs):
        client = self.connect(**kwargs)
        return client.list(directory, file_status)
