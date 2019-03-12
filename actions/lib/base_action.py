import pywhdfs.client as pywhdfs
from st2common.runners.base_action import Action


class HDFSAction(Action):

    def connect(self, nameservices_url=None, mounts=None, user=None, auth_mechanism=None, mutual_auth=None,
                max_concurrency=None, token=None, proxy=None, root=None, call_timeout=None, verify=None,
                truststore=None):
        client_kwargs = {}
        if nameservices_url is None:
            if 'nameservices_url' in self.config:
                nameservices_url = self.config["nameservices_url"]
            else:
                raise ValueError('Required configuration missing: nameservices_url')
        if mounts is None:
            if 'mounts' in self.config:
                mounts = self.config["mounts"]
            else:
                raise ValueError('Required configuration missing: mounts')
        client_kwargs["nameservices"] = [{'urls': nameservices_url, 'mounts': [mounts]}]
        if (user is None and 'user' in self.config) or user is not None:
            client_kwargs["user"] = user or self.config["user"]
        if (auth_mechanism is None and 'auth_mechanism' in self.config) or auth_mechanism is not None:
            client_kwargs["auth_mechanism"] = auth_mechanism or self.config["auth_mechanism"]
        if (verify is None and 'verify' in self.config) or verify is not None:
            client_kwargs["verify"] = verify or self.config["verify"]
        if (mutual_auth is None and 'mutual_auth' in self.config) or mutual_auth is not None:
            client_kwargs["mutual_auth"] = mutual_auth or self.config["mutual_auth"]
        if (max_concurrency is None and 'max_concurrency' in self.config) or max_concurrency is not None:
            client_kwargs["max_concurrency"] = max_concurrency or self.config["max_concurrency"]
        if (token is None and 'token' in self.config) or token is not None:
            client_kwargs["token"] = token or self.config["token"]
        if (proxy is None and 'proxy' in self.config) or proxy is not None:
            client_kwargs["proxy"] = proxy or self.config["proxy"]
        if (root is None and 'root' in self.config) or root is not None:
            client_kwargs["root"] = root or self.config["root"]
        if (call_timeout is None and 'call_timeout' in self.config) or call_timeout is not None:
            client_kwargs["timeout"] = call_timeout or self.config["call_timeout"]
        if (truststore is None and 'truststore' in self.config) or truststore is not None:
            client_kwargs["truststore"] = truststore or self.config["truststore"]
        print(client_kwargs)
        return pywhdfs.WebHDFSClient(**client_kwargs)
