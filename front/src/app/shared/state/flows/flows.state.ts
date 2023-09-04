import {Flow} from "../../../core/model/Flow";

export interface FlowState {
  flows: Flow | undefined,
  isLoading: boolean
}
