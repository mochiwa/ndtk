import { Component } from '@angular/core';
import {ProjectsPanelComponent} from "./projects-panel/projects-panel.component";
import {CommonModule} from "@angular/common";

@Component({
  standalone: true,
  selector: 'app-root',
  templateUrl: './app.component.html',
  imports: [
    ProjectsPanelComponent,
  ],
  styleUrls: ['./app.component.css']
})
export class AppComponent {
}
