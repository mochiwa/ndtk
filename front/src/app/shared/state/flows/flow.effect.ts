
import {Injectable} from "@angular/core";
import {Actions, createEffect, ofType} from "@ngrx/effects";
import {BackendService} from "../../../core/service/BackendService";
import {map, mergeMap} from "rxjs";
import {fetch, fetched} from "./flows.action";
import {GetFlowRequest} from "../../../core/model/Flow";

@Injectable({
  providedIn: 'root'
})
export class FlowEffect {
  constructor(
    private actions$: Actions,
    private backendService: BackendService
  ) {}

  fetch$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fetch),
      mergeMap((getFlowRequest:GetFlowRequest) =>
        this.backendService.getFlow(getFlowRequest.project_id, getFlowRequest.flow_id).pipe(
          map((response) => fetched({flow: response.body!})),
        )
      )
    )
  );
}
