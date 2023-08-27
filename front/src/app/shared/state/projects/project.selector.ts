import {GlobalState} from "../global-state";

export const projects = (state: GlobalState) => state?.projects?.projects
export const isLoading = (state: GlobalState) => state.projects.isLoading
