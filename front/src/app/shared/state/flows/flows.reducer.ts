import {createReducer, on} from "@ngrx/store";
import {FlowState} from "./flows.state";
import {fetch, fetched} from "./flows.action";


export const initialState: FlowState = {
  flows: undefined,
  isLoading: true
}
export const reducer = createReducer(
  initialState,
  on(fetch, (state) => {
    return {
      ...state,
      isLoading: true
    }
  }),
  on(fetched, (state, action) => {
      return {
        ...state,
        flows: action.flow,
        isLoading: false
      }
    }
  ),
)
