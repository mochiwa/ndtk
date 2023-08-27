import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatInputModule} from "@angular/material/input";
import {MatDialogModule, MatDialogRef} from "@angular/material/dialog";
import {MatButtonModule} from "@angular/material/button";
import {FormControl, FormGroup, ReactiveFormsModule} from "@angular/forms";
import {Store} from "@ngrx/store";
import {CreateProjectRequest} from "../../core/model/Project";
import {GlobalState} from "../../shared/state/global-state";
import {addProject} from "../../shared/state/projects/projects.action";

@Component({
  selector: 'app-add-project-form',
  standalone: true,
  imports: [CommonModule, MatInputModule, MatDialogModule, MatButtonModule, ReactiveFormsModule],
  templateUrl: './add-project-form.component.html',
  styleUrls: ['./add-project-form.component.css']
})
export class AddProjectFormComponent {
  projectForm = new FormGroup({
    project_name: new FormControl(''),
    nifi_uri: new FormControl(''),
  });

  constructor(
    public dialogRef: MatDialogRef<AddProjectFormComponent>,
    private store: Store<GlobalState>) {
  }

  cancel() {
    this.dialogRef.close();
  }

  submit() {
    let payload: CreateProjectRequest = Object.assign(this.projectForm.value)
    this.store.dispatch(addProject(payload))
    this.dialogRef.close();
  }
}
