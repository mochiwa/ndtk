import {createAction, props} from "@ngrx/store";
import {Flow, GetFlowRequest} from "../../../core/model/Flow";

export enum ActionTypes {
  FETCH = '[Flow Component] Fetch',
  FETCHED = '[Flow Component] Fetched'
}

export const fetch = createAction(ActionTypes.FETCH, props<GetFlowRequest>())
export const fetched = createAction(ActionTypes.FETCHED, props<{ flow: Flow }>())
