import { Component } from '@angular/core';
import {ProjectsPanelComponent} from "./projects-panel/projects-panel.component";
import {CommonModule} from "@angular/common";
import {PlaygroundComponent} from "./playground/playground.component";

@Component({
  standalone: true,
  selector: 'app-root',
  templateUrl: './app.component.html',
  imports: [
    ProjectsPanelComponent,
    PlaygroundComponent
  ],
  styleUrls: ['./app.component.css']
})
export class AppComponent {
}
