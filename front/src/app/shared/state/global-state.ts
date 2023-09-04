import {ProjectsState} from "./projects/projects.state";
import {FlowState} from "./flows/flows.state";

export interface GlobalState {
  projects: ProjectsState,
  flows : FlowState
}
