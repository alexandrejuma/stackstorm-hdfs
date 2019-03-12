import pywhdfs.client as pywhdfs
from st2common.runners.base_action import Action


class HDFSAction(Action):

    def connect(self, nameservices_url=None, mounts=None, user=None, auth_mechanism=None, mutual_auth=None,
                max_concurrency=None, token=None, proxy=None, root=None, call_timeout=None, verify=None,
                truststore=None):
        """Web HDFS client.
        :param nameservices_url: List of namenodes URL addresses to connect to. Note: Each host name should be prefixed
        with protocol and followed by WebHDFS port on namenode.
        :param mounts: mount point for it
        :param auth_mechanism: Authentication Method to use, one of 'NONE', 'GSSAPI', 'TOKEN'
        :param mutual_auth: One of "OPTIONAL", "REQUIRED", "DISABLED"
        :param max_concurrency: Max threads to allow for concurent jobs.
        :param user: The username used to connect to the cluster, valid only with NONE authentication.
        :param token: The tocken to use to authenticate when using token authentication.
        :param proxy: User to proxy as.
        :param root: Root path, this will be prefixed to all HDFS paths passed to the
          client. If the root is relative, the path will be assumed relative to the
          user's home directory.
        :param call_timeout: Connection timeouts, forwarded to the request handler. How
          long to wait for the server to send data before giving up, as a float, or a
          `(connect_timeout, read_timeout)` tuple. If the timeout is reached, an
          appropriate exception will be raised. See the requests_ documentation for
          details.
        :param verify: If the Namenode certificate should be verified or not when using SSL
           Could be a boolean True/False
        :param truststore: Path to a Truststore file.
        """
        client_kwargs = {}
        for key, value in locals().items():
            if key not in ["nameservices_url", "mounts", "self", "client_kwargs"]:
                if (value is None and key in self.config) or value is not None:
                    client_kwargs[key] = value or self.config[key]  # Call inputs have precedence over static config
        if nameservices_url is None:
            if 'nameservices_url' in self.config:
                nameservices_url = self.config["nameservices_url"]
            else:
                raise ValueError('Required configuration missing: nameservices_url.')
        if mounts is None:
            if 'mounts' in self.config:
                mounts = self.config["mounts"]
            else:
                raise ValueError('Required configuration missing: mounts')
        client_kwargs["nameservices"] = [{'urls': nameservices_url, 'mounts': [mounts]}]
        return pywhdfs.WebHDFSClient(**client_kwargs)
