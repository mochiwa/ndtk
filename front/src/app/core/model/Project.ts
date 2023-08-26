export interface Project {
  project_id: string,
  project_name: string,
  nifi_uri: string,
}

export interface CreateProjectRequest {
  project_name: string,
  nifi_uri: string,
}
