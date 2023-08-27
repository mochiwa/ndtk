import {Project} from "../../../core/model/Project";

export interface ProjectsState {
  projects: Project[],
  isLoading: boolean
}
