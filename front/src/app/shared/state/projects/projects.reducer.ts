import {ProjectsState} from "./projects.state";
import {createReducer, on} from "@ngrx/store";
import {fetchAllProjects, fetched} from "./projects.action";

export const initialState: ProjectsState = {
  projects: [],
  isLoading: true
}


export const reducer = createReducer(
  initialState,
  on(fetchAllProjects, (state) => {
    return {
      ...state,
      isLoading: true
    }
  }),
  on(fetched, (state, action) => {
      return {
        ...state,
        projects: action.projects,
        isLoading: false
      }
    }
  ),
)
