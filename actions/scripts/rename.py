from lib.base_action import HDFSAction


class HDFSRename(HDFSAction):

    def __init__(self, config):
        super(HDFSRename, self).__init__(config=config)
        self.config = config

    def run(self, hdfs_src_path, hdfs_dst_path, **kwargs):
        client = self.connect(**kwargs)
        return client.rename(hdfs_src_path, hdfs_dst_path)
