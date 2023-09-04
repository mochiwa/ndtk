import {Component, Input} from '@angular/core';
import {CommonModule} from '@angular/common';
import {MatCardModule} from "@angular/material/card";
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {Project} from "../../core/model/Project";
import {Store} from "@ngrx/store";
import {GlobalState} from "../../shared/state/global-state";
import {deleteProject} from "../../shared/state/projects/projects.action";
import {fetch} from "../../shared/state/flows/flows.action";
import {GetFlowRequest} from "../../core/model/Flow";

@Component({
  selector: 'app-project-item',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatIconModule, MatButtonModule],
  templateUrl: './project-item.component.html',
  styleUrls: ['./project-item.component.css']
})
export class ProjectItemComponent {
  collapsed = true
  @Input() project!: Project;

  constructor(private store: Store<GlobalState>) {
  }

  delete() {
    this.store.dispatch(deleteProject({project_id: this.project.project_id}))
  }

  loadFlow() {
    const request = {
      'project_id': this.project.project_id,
      'flow_id': 'root'
    } as GetFlowRequest
    console.log(request)
    this.store.dispatch(fetch(request))
  }
}
