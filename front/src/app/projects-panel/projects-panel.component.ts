import {Component, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {MatButtonModule} from "@angular/material/button";
import {MatInputModule} from "@angular/material/input";
import {Observable} from "rxjs";
import {Project} from "../core/model/Project";
import {MatDialog, MatDialogModule} from "@angular/material/dialog";
import {GlobalState} from "../shared/state/global-state";
import {Store} from "@ngrx/store";
import {projects} from "../shared/state/projects/project.selector";
import {fetchAllProjects} from "../shared/state/projects/projects.action";
import {AddProjectFormComponent} from "./add-project-form/add-project-form.component";
import {MatCardModule} from "@angular/material/card";
import {ProjectItemComponent} from "./project-item/project-item.component";

@Component({
  selector: 'projects-panel',
  standalone: true,
  imports: [CommonModule, MatButtonModule, MatInputModule, MatDialogModule, MatCardModule, ProjectItemComponent],
  templateUrl: './projects-panel.component.html',
  styleUrls: ['./projects-panel.component.css']
})
export class ProjectsPanelComponent implements OnInit {
  projects$: Observable<Project[]> = this.store.select(projects)

  constructor(public addProjectForm: MatDialog,
              private store: Store<GlobalState>) {
  }

  ngOnInit(): void {
    this.store.dispatch(fetchAllProjects())
  }

  addProject() {
    this.addProjectForm.open(AddProjectFormComponent);
  }
}
