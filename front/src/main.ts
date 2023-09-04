import {bootstrapApplication} from "@angular/platform-browser";
import {AppComponent} from "./app/app.component";
import {provideAnimations} from '@angular/platform-browser/animations';
import {provideHttpClient} from "@angular/common/http";
import {provideStore} from '@ngrx/store';
import {provideEffects} from '@ngrx/effects';
import {reducer as projectReducer} from "./app/shared/state/projects/projects.reducer";
import {ProjectEffect} from "./app/shared/state/projects/projects.effect";
import {provideStoreDevtools} from '@ngrx/store-devtools';
import {isDevMode} from '@angular/core';
import {FlowEffect} from "./app/shared/state/flows/flow.effect";
import {reducer as flowReducer} from "./app/shared/state/flows/flows.reducer";

bootstrapApplication(AppComponent, {
  providers: [
    provideAnimations(),
    provideHttpClient(),
    provideStore({projects: projectReducer, flows: flowReducer}),
    provideEffects(ProjectEffect, FlowEffect),
    provideStoreDevtools({maxAge: 25, logOnly: !isDevMode()})
  ],
})
