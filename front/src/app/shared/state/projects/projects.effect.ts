import {Actions, createEffect, ofType} from "@ngrx/effects";
import {addProject, deleteProject, fetchAllProjects, fetched} from "./projects.action";
import {map, mergeMap} from "rxjs";
import {BackendService} from "../../../core/service/BackendService";
import {Injectable} from "@angular/core";

@Injectable({
  providedIn: 'root'
})
export class ProjectEffect {
  getAll$ = createEffect(() =>
    this.actions$.pipe(
      ofType(fetchAllProjects),
      mergeMap(() => this.backendService.getAll().pipe(
          map((response) => fetched({projects: response.body!})),
        )
      )
    )
  );

  addProject$ = createEffect(()=>
    this.actions$.pipe(
      ofType(addProject),
      mergeMap((project) => this.backendService.addProject(project).pipe(
          map((response)=> fetchAllProjects())
        )
      )
    )
  );

  deleteProject$ = createEffect(()=>
    this.actions$.pipe(
      ofType(deleteProject),
      mergeMap((data) => this.backendService.deleteProject(data.project_id).pipe(
        map((response)=> fetchAllProjects())
        )
      )
    )
  );
  constructor(
    private actions$: Actions,
    private backendService: BackendService
  ) {
  }
}
