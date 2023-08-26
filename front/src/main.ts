import {bootstrapApplication} from "@angular/platform-browser";
import {AppComponent} from "./app/app.component";
import {provideAnimations} from '@angular/platform-browser/animations';
import {provideHttpClient} from "@angular/common/http";
import { provideStore } from '@ngrx/store';
import { provideEffects } from '@ngrx/effects';
import {reducer} from "./app/shared/state/projects/projects.reducer";
import {ProjectEffect} from "./app/shared/state/projects/projects.effect";
import { provideStoreDevtools } from '@ngrx/store-devtools';
import {importProvidersFrom, isDevMode} from '@angular/core';
import {CommonModule} from "@angular/common";

bootstrapApplication(AppComponent, {
  providers: [
    provideAnimations(),
    provideHttpClient(),
    provideStore({ projects: reducer }),
    provideEffects(ProjectEffect),
    provideStoreDevtools({ maxAge: 25, logOnly: !isDevMode() })
],
})
