import {GlobalState} from "../global-state";

export const flow = (state: GlobalState) => state?.flows?.flow
export const isLoading = (state: GlobalState) => state.flows.isLoading
