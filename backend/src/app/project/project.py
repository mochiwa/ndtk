class Project:

    def __init__(self, project_id: str, project_name: str, nifi_uri: str):
        self._project_id = project_id
        self._project_name = project_name
        self._nifi_uri = nifi_uri

    @property
    def project_id(self):
        return self._project_id

    @property
    def project_name(self):
        return self._project_name

    @property
    def nifi_uri(self):
        return self._nifi_uri
